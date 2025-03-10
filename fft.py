import numpy as np
import matplotlib.pyplot as plt

def compute_fft(signal, sample_rate=1.0):
    """
    Compute the Fast Fourier Transform of a signal.
    
    Parameters:
    -----------
    signal : array_like
        The input signal to transform
    sample_rate : float, optional
        The sample rate of the signal in Hz (default is 1.0)
        
    Returns:
    --------
    freqs : ndarray
        The frequency values in Hz
    fft_mag : ndarray
        The magnitude of the FFT
    """
    # Compute the FFT
    fft_result = np.fft.fft(signal)
    
    # Compute the magnitude (absolute value)
    fft_mag = np.abs(fft_result)
    
    # Compute the frequencies corresponding to the FFT bins
    n = len(signal)
    freqs = np.fft.fftfreq(n, d=1/sample_rate)
    
    # Only return the positive frequency components (since the signal is real)
    pos_mask = freqs >= 0
    return freqs[pos_mask], fft_mag[pos_mask]

def plot_fft(signal, sample_rate=1.0, title="FFT Analysis"):
    """
    Compute and plot the FFT of a signal.
    
    Parameters:
    -----------
    signal : array_like
        The input signal to transform
    sample_rate : float, optional
        The sample rate of the signal in Hz (default is 1.0)
    title : str, optional
        Title for the plot
        
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure containing the plot
    """
    # Compute the FFT
    freqs, fft_mag = compute_fft(signal, sample_rate)
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Time domain plot
    time = np.arange(len(signal)) / sample_rate
    ax1.plot(time, signal)
    ax1.set_title("Time Domain Signal")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True)
    
    # Frequency domain plot
    ax2.plot(freqs, fft_mag)
    ax2.set_title("Frequency Domain (FFT)")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Magnitude")
    ax2.grid(True)
    
    plt.tight_layout()
    plt.suptitle(title, fontsize=16)
    plt.subplots_adjust(top=0.9)
    
    return fig

def demo_fft():
    """
    Demonstrate FFT analysis with a sample signal containing multiple frequencies.
    """
    # Create a sample signal with multiple frequency components
    sample_rate = 1000  # 1 kHz sampling rate
    duration = 1.0      # 1 second duration
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Create a signal with 3 frequency components: 50 Hz, 120 Hz, and 200 Hz
    signal = (
        3.0 * np.sin(2 * np.pi * 50 * t) +   # 50 Hz component
        1.5 * np.sin(2 * np.pi * 120 * t) +  # 120 Hz component
        0.5 * np.sin(2 * np.pi * 200 * t)    # 200 Hz component
    )
    
    # Add some random noise
    noise = 0.2 * np.random.normal(size=len(t))
    signal_with_noise = signal + noise
    
    # Compute and plot the FFT
    fig = plot_fft(signal_with_noise, sample_rate, "FFT Analysis of Multi-Frequency Signal")
    
    print("FFT Analysis complete. The signal contains frequencies at:")
    print("- 50 Hz (strongest component)")
    print("- 120 Hz (medium component)")
    print("- 200 Hz (weakest component)")
    
    # Save the figure
    plt.savefig('fft_analysis.png')
    plt.show()
    
if __name__ == "__main__":
    demo_fft()
