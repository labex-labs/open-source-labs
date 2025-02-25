# Erstellen eines Canvas-Frames

Zunächst werden wir einen Canvas-Frame erstellen, in dem das Matplotlib-Diagramm dargestellt werden soll. Wir werden ein Sinus-Diagramm hinzufügen, um die Cursor-Funktionalität zu demonstrieren.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, ):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        # Erstellen Sie eine Figur und fügen Sie ein Subplot hinzu
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        # Zeichnen Sie die Sinuskurve
        self.axes.plot(t, s)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('sin(t)')

        # Erstellen Sie einen FigureCanvas, um das Diagramm anzuzeigen
        self.figure_canvas = FigureCanvas(self, -1, self.figure)

        # Binden Sie das motion_notify_event, um die Statuszeile zu aktualisieren
        self.figure_canvas.mpl_connect(
           'motion_notify_event', self.UpdateStatusBar)

        # Binden Sie das enter_window-Ereignis, um den Cursor zu ändern
        self.figure_canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # Erstellen Sie einen Sizer und fügen Sie den FigureCanvas hinzu
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.figure_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        # Erstellen Sie eine Statuszeile, um die Cursor-Position anzuzeigen
        self.statusBar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusBar)

        # Erstellen Sie eine Symbolleiste, um das Diagramm zu navigieren
        self.toolbar = NavigationToolbar2Wx(self.figure_canvas)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Show()
```
