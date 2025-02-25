# Agregar líneas verticales

En este paso, agregaremos líneas verticales al gráfico. Usaremos la función `vlines` de Matplotlib para dibujar las líneas verticales. También usaremos el parámetro `transform` para establecer que las coordenadas y se escalen de 0 a 1. Dibujaremos dos líneas verticales en x = 1 y x = 2.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
