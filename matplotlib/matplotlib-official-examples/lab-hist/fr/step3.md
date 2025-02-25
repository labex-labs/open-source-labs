# Tracer un histogramme 2D

Pour tracer un histogramme 2D, il suffit d'avoir deux vecteurs de même longueur, correspondant à chaque axe de l'histogramme.

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
