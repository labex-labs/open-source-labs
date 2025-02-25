# Den Plot erstellen

Jetzt werden wir den Plot mit `matplotlib` erstellen. Wir werden die drei Sinuswellen auf dem gleichen Graphen plotten und die Sichtbarkeit der ersten Welle auf `False` setzen, da wir sie zu Beginn versteckt lassen möchten.

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```
