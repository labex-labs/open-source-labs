# Trazar un histograma bidimensional

Para trazar un histograma bidimensional, solo se necesita dos vectores de la misma longitud, correspondientes a cada eje del histograma.

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
