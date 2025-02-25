# Crear un marco de lienzo

Primero, crearemos un marco de lienzo que contendrá el trazado de Matplotlib. Agregaremos un trazado senoidal para demostrar la funcionalidad del cursor.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, ):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        # Crear una Figura y agregar un subtrayado
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        # Trazar la curva senoidal
        self.axes.plot(t, s)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('sin(t)')

        # Crear un FigureCanvas para mostrar el trazado
        self.figure_canvas = FigureCanvas(self, -1, self.figure)

        # Vincular el evento motion_notify_event para actualizar la barra de estado
        self.figure_canvas.mpl_connect(
           'motion_notify_event', self.UpdateStatusBar)

        # Vincular el evento enter_window para cambiar el cursor
        self.figure_canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # Crear un sizer y agregar el FigureCanvas a él
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.figure_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        # Crear una barra de estado para reportar la ubicación del cursor
        self.statusBar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusBar)

        # Crear una barra de herramientas para navegar por el trazado
        self.toolbar = NavigationToolbar2Wx(self.figure_canvas)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Show()
```
