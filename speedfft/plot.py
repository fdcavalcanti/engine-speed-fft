import numpy as np
import matplotlib.pyplot as plt


def plot_peak_fft(fft_amplitude: np.ndarray, fft_frequency: np.ndarray, peaks: list=None):
    """ Plot the FFT with or without peaks marking."""
    _, ax = plt.subplots()
    ax.plot(fft_frequency, fft_amplitude)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Amplitude")
    ax.set_title("FFT Plot of Acceleration Data")
    if peaks is not None:
        ax.plot(fft_frequency[peaks], fft_amplitude[peaks], "x")
    plt.show()


def plot_time_data(data: np.ndarray):
    """ Plot acceleration data on the time domain."""
    _, ax = plt.subplots()
    ax.plot(data)
    ax.set_xlabel("Sample (n)")
    ax.set_ylabel("Amplitude (g)")
    ax.set_title("Acceleration Data")
    plt.show()
