# Hello World by Claude

A simple "Hello World" demonstration repository created with Claude's assistance.

## Description

This repository contains:
- A basic Python script that prints "Hello, World!" to the console
- Fast Fourier Transform (FFT) implementation for signal analysis

## How to Run Hello World

1. Make sure you have Python installed on your system
2. Clone this repository:
   ```
   git clone https://github.com/manncodes/hello-world-by-claude.git
   ```
3. Navigate to the repository directory:
   ```
   cd hello-world-by-claude
   ```
4. Run the script:
   ```
   python hello_world.py
   ```

## FFT Analysis Tool

The repository includes a Fast Fourier Transform (FFT) implementation for analyzing signals in the frequency domain.

### Dependencies

To run the FFT analysis, you'll need:
- NumPy
- Matplotlib

You can install these dependencies with:
```
pip install numpy matplotlib
```

### How to Use the FFT Tool

1. Run the FFT demo:
   ```
   python fft.py
   ```
   This will generate a sample signal containing multiple frequencies with some noise, compute its FFT, and display the results.

2. Use in your own code:
   ```python
   from fft import compute_fft, plot_fft
   
   # Create or load your signal
   import numpy as np
   sample_rate = 1000  # Hz
   t = np.linspace(0, 1, sample_rate)
   signal = np.sin(2 * np.pi * 10 * t)  # 10 Hz sine wave
   
   # Compute FFT
   freqs, magnitudes = compute_fft(signal, sample_rate)
   
   # Plot original signal and its FFT
   plot_fft(signal, sample_rate, "My Signal Analysis")
   ```

## The Math Behind FFT

The Fast Fourier Transform (FFT) is an algorithm that computes the Discrete Fourier Transform (DFT) efficiently. The DFT converts a signal from the time domain to the frequency domain.

For a sequence of N complex numbers x₀, x₁, ..., x_{N-1}, the DFT is defined as:

X_k = Σ_{n=0}^{N-1} x_n * e^{-i2πkn/N}

Where:
- X_k is the k-th frequency component (k = 0, 1, ..., N-1)
- x_n is the n-th time sample
- e^{-i2πkn/N} is the complex exponential (representing sinusoids)

The FFT reduces the computational complexity from O(N²) to O(N log N), making it practical for large datasets.

## Expected Output

When you run the Hello World script, you should see:
```
Hello, World!
```

When you run the FFT analysis, you'll see plots of:
1. The time-domain signal
2. The frequency-domain representation (FFT)

The demo identifies frequency components at 50 Hz, 120 Hz, and 200 Hz.

## License

This project is open source and available under the [MIT License](LICENSE).
