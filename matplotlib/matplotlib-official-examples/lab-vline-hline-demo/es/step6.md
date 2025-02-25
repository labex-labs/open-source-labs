# Agregar líneas horizontales

En este paso, agregaremos líneas horizontales al gráfico. Usaremos la función `hlines` de Matplotlib para dibujar las líneas horizontales. Dibujaremos líneas horizontales en y = 0,5, y = 2,5 y y = 4,5.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
