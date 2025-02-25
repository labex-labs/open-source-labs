# Créer une trame de canevas

Tout d'abord, nous allons créer une trame de canevas qui contiendra le tracé Matplotlib. Nous ajouterons un tracé sinusoïdal pour démontrer la fonctionnalité du curseur.

```python
class CanvasFrame(wx.Frame):
    def __init__(self, ):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        # Créer une Figure et ajouter un sous-graphe
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        # Tracer la courbe sinusoïdale
        self.axes.plot(t, s)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('sin(t)')

        # Créer un FigureCanvas pour afficher le tracé
        self.figure_canvas = FigureCanvas(self, -1, self.figure)

        # Lier l'événement motion_notify_event pour mettre à jour la barre de statut
        self.figure_canvas.mpl_connect(
           'motion_notify_event', self.UpdateStatusBar)

        # Lier l'événement enter_window pour changer le curseur
        self.figure_canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # Créer un sizer et ajouter le FigureCanvas à celui-ci
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.figure_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

        # Créer une barre de statut pour rapporter l'emplacement du curseur
        self.statusBar = wx.StatusBar(self, -1)
        self.SetStatusBar(self.statusBar)

        # Créer une barre d'outils pour naviguer dans le tracé
        self.toolbar = NavigationToolbar2Wx(self.figure_canvas)
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Show()
```
