# Tracer des histogrammes et des noyaux

Nous traçons d'abord des histogrammes et des noyaux pour démontrer la différence entre les deux. Nous utiliserons une estimation de la densité de noyau gaussienne pour montrer la différence entre les deux. Nous comparerons également d'autres noyaux disponibles dans scikit-learn.

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

# Generate data
np.random.seed(1)
N = 20
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
bins = np.linspace(-5, 10, 10)

# Create figure and axes
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.05, wspace=0.05)

# Plot histogram 1
ax[0, 0].hist(X[:, 0], bins=bins, fc="#AAAAFF", density=True)
ax[0, 0].text(-3.5, 0.31, "Histogramme")

# Plot histogram 2
ax[0, 1].hist(X[:, 0], bins=bins + 0.75, fc="#AAAAFF", density=True)
ax[0, 1].text(-3.5, 0.31, "Histogramme, bins décalés")

# Plot tophat KDE
kde = KernelDensity(kernel="tophat", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 0].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 0].text(-3.5, 0.31, "Densité de noyau tophat")

# Plot Gaussian KDE
kde = KernelDensity(kernel="gaussien", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 1].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 1].text(-3.5, 0.31, "Densité de noyau gaussienne")

# Plot data points
for axi in ax.ravel():
    axi.plot(X[:, 0], np.full(X.shape[0], -0.01), "+k")
    axi.set_xlim(-4, 9)
    axi.set_ylim(-0.02, 0.34)

# Set y-axis label for left column
for axi in ax[:, 0]:
    axi.set_ylabel("Densité normalisée")

# Set x-axis label for bottom row
for axi in ax[1, :]:
    axi.set_xlabel("x")

# Show plot
plt.show()
```
