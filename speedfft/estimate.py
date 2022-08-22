import argparse
import csv
import numpy as np
import os
import sys
from scipy.signal import find_peaks
from plot import plot_peak_fft, plot_time_data


def fft_axis(acceleration_data: np.ndarray, sample_freq: int=100, filter: bool=False) -> np.ndarray:
    """ Remove the mean and calculate the FFT of acceleration_data.
        Return both the FFT and frequency axis data for plotting.
    """
    data_length = len(acceleration_data)
    if filter:
        print("Removing mean from acceleration data")
        acceleration_data = acceleration_data - np.mean(acceleration_data)
    fft_data = np.fft.rfft(acceleration_data)/data_length
    fft_data = 2*np.abs(fft_data)
    frequency_axis = np.fft.fftfreq(data_length, d=1/sample_freq)
    return fft_data[:data_length//2], frequency_axis[:data_length//2]


def find_fft_peak(fft_data, height_compare: float=1.5):
    """ Return the index of peaks on FFT data. Use the height_compare
        value to establish the height threshold. Default is to return
        peaks of 1.5x the mean amplitude.
    """
    idx = find_peaks(fft_data, height=height_compare*np.mean(fft_data))
    if len(idx[0]) == 0:
        print("Peaks not found")
        return None
    return idx[0]


def read_accelerometer_data(file_path: str):
    """ Read accelerometer data from a file.
        Data must be on CSV format. Example:

        datax,datay,dataz
        0.001,0.002,0.003
    """
    x_data, y_data, z_data = [], [], []
    num_axis = 0
    print("Importing data")
    with open(file_path, "r", encoding="utf-8") as file:
        file_data = csv.reader(file)
        for idx, row in enumerate(file_data):
            if idx == 0:
                columns = len(row)  # Estimate columns available
                num_axis = columns
                print(f"Found {columns} columns")
            x_data.append(row[0])
            if num_axis > 1:
                y_data.append(row[1])
                if num_axis > 2:
                    z_data.append(row[2])

    x_data = np.asarray(x_data, dtype=np.float32)
    y_data = np.asarray(y_data, dtype=np.float32)
    z_data = np.asarray(z_data, dtype=np.float32)
    return x_data, y_data, z_data


def estimate_engine_speed(frequency: np.ndarray, cylinders: int=4) -> float:
    """ Estime engine speed based on peak frequency and cylinders."""
    engine_speed = 60*frequency/2
    return engine_speed


def main(datalog_path):
    """ Executes the script to estimate engine speed from acceleration data."""
    x_data, y_data, z_data = read_accelerometer_data(datalog_path)
    fft_data_x, fft_freq = fft_axis(x_data, filter=True)
    peaks = find_fft_peak(fft_data_x, height_compare=4)
    frequency_peaks = fft_freq[peaks]
    for peak in frequency_peaks:
        espeed = estimate_engine_speed(peak)
        print(f"Engine speed estimated: {np.round(espeed, 2)} RPM")
    plot_peak_fft(fft_data_x, fft_freq, peaks)
    plot_time_data(x_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate engine speed using data from\
                                                  accelerometer")
    parser.add_argument("--filepath", default=None,
                        help="Absolute path for datalog to be used (default: example file)")
    args = parser.parse_args()
    if args.filepath is not None:
        log_file = args.filepath
    else:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        log_file = os.path.join(os.path.dirname(current_dir), "data", "sample_idle_data.csv")

    print(f"File: {log_file}")
    if not os.path.exists(log_file):
        print("File not found")
        sys.exit(0)
    main(log_file)
