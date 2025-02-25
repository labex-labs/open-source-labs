# Definir la clase FourierDemoFrame

La clase FourierDemoFrame creará la interfaz gráfica de usuario (GUI) utilizando wxPython y Matplotlib.

```python
class FourierDemoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        panel = wx.Panel(self)

        # crear los elementos de la GUI
        self.createCanvas(panel)
        self.createSliders(panel)

        # colocarlos en un sizer para el diseño
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.frequencySliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, borde=5)
        sizer.Add(self.amplitudeSliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, borde=5)
        panel.SetSizer(sizer)

    def createCanvas(self, padre):
        self.lines = []
        self.figure = Figure()
        self.canvas = FigureCanvas(padre, -1, self.figure)
        self.canvas.callbacks.connect('button_press_event', self.mouseDown)
        self.canvas.callbacks.connect('motion_notify_event', self.mouseMotion)
        self.canvas.callbacks.connect('button_release_event', self.mouseUp)
        self.state = ''
        self.mouseInfo = (None, None, None, None)
        self.f0 = Param(2., mínimo=0., máximo=6.)
        self.A = Param(1., mínimo=0.01, máximo=2.)
        self.createPlots()

        self.f0.attach(self)
        self.A.attach(self)

    def createSliders(self, panel):
        self.frequencySliderGroup = SliderGroup(
            panel,
            etiqueta='Frecuencia f0:',
            param=self.f0)
        self.amplitudeSliderGroup = SliderGroup(panel, etiqueta='Amplitud a:',
                                                param=self.A)

    def mouseDown(self, evento):
        if self.lines[0].contains(evento)[0]:
            self.state = 'frecuencia'
        elif self.lines[1].contains(evento)[0]:
            self.state = 'tiempo'
        else:
            self.state = ''
        self.mouseInfo = (evento.xdata, evento.ydata,
                          max(self.f0.value,.1),
                          self.A.value)

    def mouseMotion(self, evento):
        if self.state == '':
            return
        x, y = evento.xdata, evento.ydata
        if x is None:  # fuera de los ejes
            return
        x0, y0, f0Init, AInit = self.mouseInfo
        self.A.set(AInit + (AInit * (y - y0) / y0), self)
        if self.state == 'frecuencia':
            self.f0.set(f0Init + (f0Init * (x - x0) / x0))
        elif self.state == 'tiempo':
            if (x - x0) / x0!= -1.:
                self.f0.set(1. / (1. / f0Init + (1. / f0Init * (x - x0) / x0)))

    def mouseUp(self, evento):
        self.state = ''

    def createPlots(self):
        self.subplot1, self.subplot2 = self.figure.subplots(2)
        x1, y1, x2, y2 = self.compute(self.f0.value, self.A.value)
        color = (1., 0., 0.)
        self.lines += self.subplot1.plot(x1, y1, color=color, linewidth=2)
        self.lines += self.subplot2.plot(x2, y2, color=color, linewidth=2)
        self.subplot1.set_title(
            "Haga clic y arrastre las formas de onda para cambiar la frecuencia y la amplitud",
            fontsize=12)
        self.subplot1.set_ylabel("Forma de onda en el dominio de la frecuencia X(f)", fontsize=8)
        self.subplot1.set_xlabel("frecuencia f", fontsize=8)
        self.subplot2.set_ylabel("Forma de onda en el dominio del tiempo x(t)", fontsize=8)
        self.subplot2.set_xlabel("tiempo t", fontsize=8)
        self.subplot1.set_xlim([-6, 6])
        self.subplot1.set_ylim([0, 1])
        self.subplot2.set_xlim([-2, 2])
        self.subplot2.set_ylim([-2, 2])
        self.subplot1.text(0.05,.95,
                           r'$X(f) = \mathcal{F}\{x(t)\}$',
                           verticalalignment='top',
                           transform=self.subplot1.transAxes)
        self.subplot2.text(0.05,.95,
                           r'$x(t) = a \cdot \cos(2\pi f_0 t) e^{-\pi t^2}$',
                           verticalalignment='top',
                           transform=self.subplot2.transAxes)

    def compute(self, f0, A):
        f = np.arange(-6., 6., 0.02)
        t = np.arange(-2., 2., 0.01)
        x = A * np.cos(2 * np.pi * f0 * t) * np.exp(-np.pi * t ** 2)
        X = A / 2 * \
            (np.exp(-np.pi * (f - f0) ** 2) + np.exp(-np.pi * (f + f0) ** 2))
        return f, X, t, x

    def setKnob(self, value):
        x1, y1, x2, y2 = self.compute(self.f0.value, self.A.value)
        self.lines[0].set(xdata=x1, ydata=y1)
        self.lines[1].set(xdata=x2, ydata=y2)
        self.canvas.draw()
```
