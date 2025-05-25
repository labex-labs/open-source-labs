# Alterar o Gráfico

Defina uma função que altera o gráfico com base na função selecionada. Esta função recebe um `plot_number` como entrada e altera o gráfico de acordo.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
