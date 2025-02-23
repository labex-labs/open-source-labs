# Créer un graphique

Ensuite, nous allons créer un graphique à l'aide de Matplotlib. Dans cet exemple, nous allons tracer la fonction cosinus sur une plage de valeurs.

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```
