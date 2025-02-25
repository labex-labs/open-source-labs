# Crear un gráfico symlog en ambos el eje x y el eje y

En el tercer subgráfico, crearemos un gráfico `symlog` en tanto el eje x como el eje y. También estableceremos el parámetro `linthresh` en 0.015.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
