# Graficar datos

Ahora podemos graficar nuestros datos usando la función `plot`. Crearemos dos líneas usando los datos que creamos en el paso 3.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
