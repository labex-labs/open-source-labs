# Crear la gráfica de Matplotlib

En este paso, crearemos una gráfica de Matplotlib que mostrará nuestros datos. Empezaremos creando una figura y agregando un subgráfico.

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```
