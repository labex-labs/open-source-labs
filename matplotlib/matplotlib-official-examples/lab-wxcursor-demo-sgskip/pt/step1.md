# Criar um Canvas Frame

Primeiramente, criaremos um canvas frame que conterá o gráfico Matplotlib. Adicionaremos um gráfico senoidal para demonstrar a funcionalidade do cursor.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, ):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        # Create a Figure and add a subplot
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        # Plot the sinusoidal curve
        self.axes.plot(t, s)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('sin(t)')

        # Create a FigureCanvas to display the plot
        self.figure_canvas = FigureCanvas(self, -1, self.figure)

        # Bind the motion_notify_event to update the status bar
        self.figure_canvas.mpl_connect(
            'motion_notify_event', self.UpdateStatusBar)

        # Bind the enter_window event to change the cursor
        self.figure_canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # Create a sizer and add the FigureCanvas to it
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.figure_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        # Create a status bar to report the cursor location
        self.statusBar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusBar)

        # Create a toolbar to navigate the plot
        self.toolbar = NavigationToolbar2Wx(self.figure_canvas)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Show()
```
