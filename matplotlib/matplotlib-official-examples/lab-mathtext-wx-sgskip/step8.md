# Change the Plot

Define a function that changes the plot based on the selected function. This function takes a plot_number as input and changes the plot accordingly.

```python
    def change_plot(self, plot_number):
        t = np.arange(1.0, 3.0, 0.01)
        s = functions[plot_number][1](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()
```
