# Ajouter des données au graphique

Enfin, vous pouvez ajouter des données au graphique pour les visualiser. Dans ce cas, vous pouvez utiliser la fonction `plot()` pour tracer une onde sinusoïdale.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
