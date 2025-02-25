# Cambiar la gráfica

Define una función que cambia la gráfica según la función seleccionada. Esta función toma un plot_number como entrada y cambia la gráfica en consecuencia.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
