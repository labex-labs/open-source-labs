# Créer des lignes et une légende

Nous allons créer deux lignes et une légende à l'aide de Matplotlib.

```python
line1, = ax.plot(t, y1, lw=2, label='1 Hz')
line2, = ax.plot(t, y2, lw=2, label='2 Hz')
leg = ax.legend(fancybox=True, shadow=True)
```
