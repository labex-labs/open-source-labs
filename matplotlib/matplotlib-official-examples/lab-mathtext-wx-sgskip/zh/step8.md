# 更改绘图

定义一个函数，该函数根据所选函数更改绘图。此函数将一个绘图编号作为输入，并相应地更改绘图。

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
