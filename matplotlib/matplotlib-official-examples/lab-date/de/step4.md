# Daten plotten

Wir werden die Daten auf allen drei Subplots mit der `plot`-Funktion plotten.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Preis [\$]')
```
