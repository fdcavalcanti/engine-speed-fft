import matplotlib.pyplot as plt
import numpy as np
import unittest
from speedfft.speedfft import fft_axis, find_fft_peak


def generate_test_signal(frequency: int, sample_rate: int=100, samples: int=1000):
    """ Generate a simple sine wave and return time and signal data."""
    time = np.linspace(0, samples/sample_rate, samples)
    signal = np.sin(2*np.pi*frequency*time)
    return time, signal


class TestFFT(unittest.TestCase):
    """ Test the FFT functionality."""
    def test_single_peak(self):
        """ Test peak FFT return value for a single peak."""
        test_freq = 42
        _, signal = generate_test_signal(test_freq)
        data, freq = fft_axis(signal)
        peaks = find_fft_peak(data)
        peak_freq = int(freq[peaks[0]])
        print(f"FFT Peaks data: {peaks}")
        print(f"Peak Frequency: {peak_freq}")
        self.assertEqual(peak_freq, test_freq)

    def test_multiple_peaks(self):
        """ Test if multiple peaks are identified."""
        test_freq = [10, 25, 40]
        samples = 1000
        signal_sum = np.zeros(samples)
        for frequency in test_freq:
            _, signal = generate_test_signal(frequency)
            signal_sum += signal

        data, freq = fft_axis(signal_sum)
        peaks = list(find_fft_peak(data))
        peaks_hz = list(freq[peaks])
        print(f"Peaks: {peaks_hz} Hz")
        self.assertListEqual(test_freq, peaks_hz)


if __name__ == "__main__":
    unittest.main()
