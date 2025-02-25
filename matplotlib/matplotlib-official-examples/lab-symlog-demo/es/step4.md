# Crear un gráfico symlog en el eje x

En el primer subgráfico, crearemos un gráfico `symlog` en el eje x. También agregaremos una cuadrícula menor al eje x.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```
