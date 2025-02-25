# Создайте рамку для холста

Сначала мы создадим рамку для холста, которая будет содержать график Matplotlib. Мы добавим синусоидальный график, чтобы продемонстрировать функцию курсора.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, ):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        # Создайте Figure и добавьте подграфик
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        # Постройте синусоидальную кривую
        self.axes.plot(t, s)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('sin(t)')

        # Создайте FigureCanvas для отображения графика
        self.figure_canvas = FigureCanvas(self, -1, self.figure)

        # Привяжите motion_notify_event для обновления статусной строки
        self.figure_canvas.mpl_connect(
           'motion_notify_event', self.UpdateStatusBar)

        # Привяжите enter_window событие для изменения курсора
        self.figure_canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # Создайте размерщик и добавьте FigureCanvas в него
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.figure_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        # Создайте статусную строку для отчета о расположении курсора
        self.statusBar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusBar)

        # Создайте панель инструментов для навигации по графику
        self.toolbar = NavigationToolbar2Wx(self.figure_canvas)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Show()
```
