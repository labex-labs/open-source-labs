# Измените график

Определите функцию, которая изменяет график в зависимости от выбранной функции. Эта функция принимает plot_number в качестве входных данных и изменяет график в соответствии с ними.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
