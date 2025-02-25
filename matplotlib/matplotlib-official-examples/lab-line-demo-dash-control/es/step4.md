# Crear la gráfica

Ahora, podemos crear la gráfica usando la función `plt.subplots()`. También crearemos tres líneas usando la función `ax.plot()`.

```python
fig, ax = plt.subplots()

# Usando set_dashes() y set_capstyle() para modificar el trazo de una línea existente.
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # Línea de 2pt, ruptura de 2pt, línea de 10pt, ruptura de 2pt.
line1.set_dash_capstyle('round')

# Usando plot(..., dashes=...) para establecer el trazo al crear una línea.
line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

# Usando plot(..., dashes=..., gapcolor=...) para establecer el trazo y
# el color alternante al crear una línea.
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')

ax.legend(handlelength=4)
plt.show()
```
