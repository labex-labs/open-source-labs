# Plotar os dados

Plotaremos os dados em todos os três subplots usando a função `plot`.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')
```
