# Générer des données

Dans cette étape, nous allons générer de multiples séries de "signaux" sinusoidaux qui sont enterrés sous un plus grand nombre de séries de "bruit/fond" de marche aléatoire. Nous allons générer des marches aléatoires gaussiennes non biaisées et des signaux sinusoidaux.

```python
# Fix random state for reproducibility
np.random.seed(19680801)

# Make some data; a 1D random walk + small fraction of sine waves
num_series = 1000
num_points = 100
SNR = 0.10  # Signal to Noise Ratio
x = np.linspace(0, 4 * np.pi, num_points)

# Generate unbiased Gaussian random walks
Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)

# Generate sinusoidal signals
num_signal = round(SNR * num_series)
phi = (np.pi / 8) * np.random.randn(num_signal, 1)  # small random offset
Y[-num_signal:] = (
    np.sqrt(np.arange(num_points))  # random walk RMS scaling factor
    * (np.sin(x - phi)
       + 0.05 * np.random.randn(num_signal, num_points))  # small random noise
)
```
