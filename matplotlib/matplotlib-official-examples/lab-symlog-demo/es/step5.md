# Crear un gráfico symlog en el eje y

En el segundo subgráfico, crearemos un gráfico `symlog` en el eje y.

```python
ax1.plot(y1, x)
ax1.set_yscale('symlog')
ax1.set_ylabel('symlogy')
```
