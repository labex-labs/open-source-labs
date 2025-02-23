# Crear un gráfico log-log con datalim ajustable

A continuación, crearemos un gráfico log-log con un datalim ajustable. Esto significa que tanto el eje x como el eje y tendrán escalas logarítmicas y la relación de aspecto del gráfico se ajustará para adaptarse a los datos.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```
