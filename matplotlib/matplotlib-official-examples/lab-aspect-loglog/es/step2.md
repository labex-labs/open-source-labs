# Crear un gráfico log-log con caja ajustable

A continuación, crearemos un gráfico log-log con una caja ajustable. Esto significa que tanto el eje x como el eje y tendrán escalas logarítmicas y la relación de aspecto del gráfico será igual a 1.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```
