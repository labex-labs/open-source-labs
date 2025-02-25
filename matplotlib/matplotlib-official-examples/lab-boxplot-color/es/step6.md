# Agregando líneas de cuadrícula horizontales

Finalmente, agregaremos líneas de cuadrícula horizontales a los diagramas de caja utilizando la función `yaxis.grid()`.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Tres Muestras Separadas')
    ax.set_ylabel('Valores Observados')

plt.show()
```
