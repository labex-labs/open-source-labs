# Darstellung von Histogrammen und Kernen

Wir zeichnen zunächst Histogramme und Kerne, um den Unterschied zwischen den beiden zu demonstrieren. Wir werden eine Gaußsche Kernel-Dichteschätzung verwenden, um den Unterschied zwischen den beiden zu zeigen. Wir werden auch andere Kerne vergleichen, die in scikit-learn verfügbar sind.

```python
# Import notwendige Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

# Generiere Daten
np.random.seed(1)
N = 20
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
bins = np.linspace(-5, 10, 10)

# Erstelle Figur und Achsen
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.05, wspace=0.05)

# Zeichne Histogramm 1
ax[0, 0].hist(X[:, 0], bins=bins, fc="#AAAAFF", density=True)
ax[0, 0].text(-3.5, 0.31, "Histogramm")

# Zeichne Histogramm 2
ax[0, 1].hist(X[:, 0], bins=bins + 0.75, fc="#AAAAFF", density=True)
ax[0, 1].text(-3.5, 0.31, "Histogramm, Bins verschoben")

# Zeichne Tophat-KDE
kde = KernelDensity(kernel="tophat", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 0].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 0].text(-3.5, 0.31, "Tophat-Kernel-Dichte")

# Zeichne Gaußsche KDE
kde = KernelDensity(kernel="gaussian", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 1].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 1].text(-3.5, 0.31, "Gaußsche Kernel-Dichte")

# Zeichne Datenpunkte
for axi in ax.ravel():
    axi.plot(X[:, 0], np.full(X.shape[0], -0.01), "+k")
    axi.set_xlim(-4, 9)
    axi.set_ylim(-0.02, 0.34)

# Setze y-Achsenbeschriftung für die linke Spalte
for axi in ax[:, 0]:
    axi.set_ylabel("Normalisierte Dichte")

# Setze x-Achsenbeschriftung für die untere Zeile
for axi in ax[1, :]:
    axi.set_xlabel("x")

# Zeige das Diagramm an
plt.show()
```
