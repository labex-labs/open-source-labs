# Définition de la classe FourierDemoFrame

La classe FourierDemoFrame créera l'interface graphique utilisateur (GUI) à l'aide de wxPython et Matplotlib.

```python
class FourierDemoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        panel = wx.Panel(self)

        # créer les éléments de l'interface graphique
        self.createCanvas(panel)
        self.createSliders(panel)

        # les placer dans un sizer pour la mise en page
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.frequencySliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.amplitudeSliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(sizer)

    def createCanvas(self, parent):
        self.lines = []
        self.figure = Figure()
        self.canvas = FigureCanvas(parent, -1, self.figure)
        self.canvas.callbacks.connect('button_press_event', self.mouseDown)
        self.canvas.callbacks.connect('motion_notify_event', self.mouseMotion)
        self.canvas.callbacks.connect('button_release_event', self.mouseUp)
        self.state = ''
        self.mouseInfo = (None, None, None, None)
        self.f0 = Param(2., minimum=0., maximum=6.)
        self.A = Param(1., minimum=0.01, maximum=2.)
        self.createPlots()

        self.f0.attach(self)
        self.A.attach(self)

    def createSliders(self, panel):
        self.frequencySliderGroup = SliderGroup(
            panel,
            label='Fréquence f0 :',
            param=self.f0)
        self.amplitudeSliderGroup = SliderGroup(panel, label=' Amplitude a :',
                                                param=self.A)

    def mouseDown(self, event):
        if self.lines[0].contains(event)[0]:
            self.state = 'fréquence'
        elif self.lines[1].contains(event)[0]:
            self.state = 'temps'
        else:
            self.state = ''
        self.mouseInfo = (event.xdata, event.ydata,
                          max(self.f0.value,.1),
                          self.A.value)

    def mouseMotion(self, event):
        if self.state == '':
            return
        x, y = event.xdata, event.ydata
        if x is None:  # en dehors des axes
            return
        x0, y0, f0Init, AInit = self.mouseInfo
        self.A.set(AInit + (AInit * (y - y0) / y0), self)
        if self.state == 'fréquence':
            self.f0.set(f0Init + (f0Init * (x - x0) / x0))
        elif self.state == 'temps':
            if (x - x0) / x0!= -1.:
                self.f0.set(1. / (1. / f0Init + (1. / f0Init * (x - x0) / x0)))

    def mouseUp(self, event):
        self.state = ''

    def createPlots(self):
        self.subplot1, self.subplot2 = self.figure.subplots(2)
        x1, y1, x2, y2 = self.compute(self.f0.value, self.A.value)
        couleur = (1., 0., 0.)
        self.lines += self.subplot1.plot(x1, y1, couleur=couleur, linewidth=2)
        self.lines += self.subplot2.plot(x2, y2, couleur=couleur, linewidth=2)
        self.subplot1.set_title(
            "Cliquez et faites glisser les formes d'onde pour changer la fréquence et l'amplitude",
            fontsize=12)
        self.subplot1.set_ylabel("Forme d'onde dans le domaine de la fréquence X(f)", fontsize=8)
        self.subplot1.set_xlabel("fréquence f", fontsize=8)
        self.subplot2.set_ylabel("Forme d'onde dans le domaine du temps x(t)", fontsize=8)
        self.subplot2.set_xlabel("temps t", fontsize=8)
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
