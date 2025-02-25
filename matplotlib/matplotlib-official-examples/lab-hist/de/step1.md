# Daten generieren und ein einfaches Histogramm zeichnen

Um ein eindimensionales Histogramm zu generieren, benötigen wir nur einen einzigen Vektor von Zahlen. Für ein zweidimensionales Histogramm benötigen wir einen zweiten Vektor. Wir werden beide unten generieren und das Histogramm für jeden Vektor anzeigen.

```python
import matplotlib.pyplot as plt
import numpy as np

# Erstellen eines Zufallszahlengenerators mit einem feste Seed für Wiederholbarkeit
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# Generieren von zwei Normalverteilungen
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# Wir können die Anzahl der Bins mit dem Schlüsselwortargument *bins* festlegen.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```
