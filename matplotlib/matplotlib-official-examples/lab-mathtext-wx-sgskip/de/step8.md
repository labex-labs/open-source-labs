# Ändern des Diagramms

Definieren Sie eine Funktion, die das Diagramm basierend auf der ausgewählten Funktion ändert. Diese Funktion nimmt eine plot_number als Eingabe und ändert das Diagramm entsprechend.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
