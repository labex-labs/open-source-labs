# Spécifier manuellement les couleurs des courbes de niveau

Nous pouvons également spécifier manuellement les couleurs des courbes de niveau.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6,
                linewidths=np.arange(.5, 4,.5),
                colors=('r', 'green', 'blue', (1, 1, 0), '#afeeee', '0.5'),
                )
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Crazy lines')
```
