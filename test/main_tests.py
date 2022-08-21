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
    def test_fft_peak(self):
        """ Test peak FFT return value."""
        test_freq = 42
        _, signal = generate_test_signal(test_freq)
        data, freq = fft_axis(signal)
        peaks = find_fft_peak(data)
        peak_freq = int(freq[peaks[0][0]])
        print(f"FFT Peaks data: {peaks}")
        print(f"Peak Frequency: {peak_freq}")
        self.assertEqual(peak_freq, test_freq)


if __name__ == "__main__":
    unittest.main()
