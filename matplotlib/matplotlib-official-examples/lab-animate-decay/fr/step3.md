# Préparer le tracé

Maintenant, nous devons préparer le tracé. Nous allons créer une figure et un objet d'axes à l'aide de la fonction `subplots()` de Matplotlib. Nous allons également créer un objet de ligne pour représenter l'onde sinusoïdale.

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```
