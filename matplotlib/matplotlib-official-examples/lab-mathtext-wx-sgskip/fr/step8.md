# Changer le tracé

Définissez une fonction qui change le tracé en fonction de la fonction sélectionnée. Cette fonction prend un plot_number en entrée et change le tracé en conséquence.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
