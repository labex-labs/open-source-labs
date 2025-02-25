# Tracer le graphique

Nous allons maintenant tracer le graphique en utilisant `np.linspace` et `np.sin`.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
