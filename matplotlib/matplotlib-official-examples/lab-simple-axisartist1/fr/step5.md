# Tracer les données

Maintenant que nous avons créé nos sous-graphiques, nous pouvons tracer nos données en utilisant `np.sin(x)`.

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```
