# Создайте рамку для холста

Создайте новый класс, наследующийся от wx.Frame. Этот класс создает холст, на котором отображается выбранная функция.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title, size=(550, 350))

        self.figure = Figure()
        self.axes = self.figure.add_subplot()

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.change_plot(0)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_buttonbar()
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)

        self.SetSizer(self.sizer)
        self.Fit()
```
