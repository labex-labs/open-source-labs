# Définir les données

Nous allons définir les données pour le graphique. Nous allons générer 20 valeurs aléatoires pour les rayons et les angles.

```python
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
colors = plt.cm.viridis(radii / 10.)
```
