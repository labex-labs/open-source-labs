# Graficar datos

Graficaremos los datos en los tres subgráficos utilizando la función `plot`.

```python
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    ax.grid(True)
    ax.set_ylabel(r'Precio [\$]')
```
