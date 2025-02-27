# Générer des données d'échantillonnage

Nous allons générer un signal mixte d'échantillonnage composé de trois composantes indépendantes. Nous allons ajouter du bruit au signal et standardiser les données. Nous allons également générer une matrice de mélange pour mélanger nos trois composantes indépendantes.

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # Signal 1 : signal sinusoïdal
s2 = np.sign(np.sin(3 * time))  # Signal 2 : signal carré
s3 = signal.sawtooth(2 * np.pi * time)  # Signal 3: signal en dents de scie

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # Ajouter du bruit

S /= S.std(axis=0)  # Standardiser les données
# Mélanger les données
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Matrice de mélange
X = np.dot(S, A.T)  # Générer les observations
```
