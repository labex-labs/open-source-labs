# Tracer une ligne diagonale

Tout d'abord, nous allons tracer une ligne diagonale à un angle de 45 degrés en utilisant la fonction `plot()` de Matplotlib.

```python
fig, ax = plt.subplots()

# Tracer la ligne diagonale (45 degrés)
h = ax.plot(range(0, 10), range(0, 10))
```
