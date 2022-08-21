import numpy as np
import matplotlib.pyplot as plt
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


if __name__ == "__main__":
    freq = 42
    Fs = 100
    samples = 1000
    t = np.linspace(0, samples/Fs, samples)
    signal = np.sin(2*np.pi*freq*t)

    a, b = fft_axis(signal, filter=False)
    peaks = find_fft_peak(a)[0]
    plt.plot(b, a)
    plt.plot(b[peaks], a[peaks], "*")

    plt.show()
