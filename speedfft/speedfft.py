import csv
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import find_peaks


def fft_axis(acceleration_data: np.ndarray, sample_freq: int=100, filter: bool=False) -> np.ndarray:
    """ Remove the mean and calculate the FFT of acceleration_data.
        Return both the FFT and frequency axis data for plotting.
    """
    data_length = len(acceleration_data)
    if filter:
        print("Filtering")
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
    print(len(idx[0]))
    if len(idx[0]) == 0:
        print("Peaks not found")
        return None
    else:
        return idx[0]


def read_accelerometer_data(file_path: str):
    """ Read accelerometer data from a file.
        Data must be on CSV format. Example:

        datax,datay,dataz
        0.001,0.002,0.003
    """
    x_data, y_data, z_data = [], [], []
    with open(file_path, "r") as file:
        file_data = csv.reader(file)
        for idx, row in enumerate(file_data):
            if len(row) != 3:
                print(f"Bad parsing on line {idx}")
                return 0
            x_data.append(row[0])
            y_data.append(row[1])
            z_data.append(row[2])


if __name__ == "__main__":
    file_name = "sample_idle_data.csv"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(os.path.dirname(current_dir), "data", file_name)
    print(data_dir)
    read_accelerometer_data(data_dir)
