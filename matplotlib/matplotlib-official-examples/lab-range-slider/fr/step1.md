# Générer une image fictive

Tout d'abord, nous allons générer une image en niveaux de gris fictive à l'aide du module `random` de NumPy. Nous allons définir la graine pour vous assurer que les résultats sont reproductibles.

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
