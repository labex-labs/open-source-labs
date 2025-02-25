# Tracer les données

Nous allons tracer les données sur les trois sous-graphiques à l'aide de la fonction `plot`.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Prix [\$]')
```
