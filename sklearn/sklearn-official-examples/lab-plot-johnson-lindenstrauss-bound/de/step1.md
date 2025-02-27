# Theoretische Grenzen

Der erste Schritt besteht darin, die theoretischen Grenzen des Johnson-Lindenstrauss-Lemmas zu untersuchen. Wir werden die minimale Anzahl an Dimensionen plotten, die erforderlich sind, um eine `eps`-Einbettung für eine zunehmende Anzahl von Proben `n_samples` zu gewährleisten. Die durch einen zufälligen Projekion `p` eingeführte Verzerrung wird dadurch behauptet, dass `p` mit guter Wahrscheinlichkeit eine `eps`-Einbettung definiert, wie durch folgende Gleichung definiert:

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

Wobei `u` und `v` beliebige Zeilen aus einem Datensatz der Form `(n_samples, n_features)` sind und `p` eine Projekion durch eine zufällige Gaußsche `N(0, 1)`-Matrix der Form `(n_components, n_features)` (oder eine dünne Achlioptas-Matrix) ist.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# Bereich der zulässigen Verzerrungen
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# Bereich der Anzahl von Proben (Beobachtungen) zum Einbetten
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, color in zip(eps_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, color=color)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="lower right")
plt.xlabel("Anzahl der Beobachtungen zur eps-Einbettung")
plt.ylabel("Minimale Anzahl an Dimensionen")
plt.title("Johnson-Lindenstrauss-Grenzen:\nn_samples vs n_components")
plt.show()
```
