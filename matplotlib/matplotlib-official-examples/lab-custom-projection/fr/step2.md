# Création de la classe GeoAxes

Nous allons créer une classe de base abstraite pour les projections géographiques appelée `GeoAxes`.

```python
class GeoAxes(Axes):
    """
    Une classe de base abstraite pour les projections géographiques
    """

    class ThetaFormatter(Formatter):
        """
        Utilisée pour formater les étiquettes d'échelonnage en theta. Convertit
        l'unité native en radians en degrés et ajoute un symbole de degré.
        """
        def __init__(self, round_to=1.0):
            self._round_to = round_to

        def __call__(self, x, pos=None):
            degrees = round(np.rad2deg(x) / self._round_to) * self._round_to
            return f"{degrees:0.0f}\N{DEGREE SIGN}"

    RESOLUTION = 75

    def _init_axis(self):
        self.xaxis = maxis.XAxis(self)
        self.yaxis = maxis.YAxis(self)
        # Ne pas enregistrer xaxis ou yaxis avec les épines - comme dans
        # Axes._init_axis() - jusqu'à ce que GeoAxes.xaxis.clear() fonctionne.
        # self.spines['geo'].register_axis(self.yaxis)

    def clear(self):
        # docstring héritée
        super().clear()

        self.set_longitude_grid(30)
        self.set_latitude_grid(15)
        self.set_longitude_grid_ends(75)
        self.xaxis.set_minor_locator(NullLocator())
        self.yaxis.set_minor_locator(NullLocator())
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')
        self.yaxis.set_tick_params(label1On=True)
        # Pourquoi devons-nous activer les étiquettes d'échelonnage de l'axe y, mais
        # les étiquettes d'échelonnage de l'axe x sont déjà activées?

        self.grid(rcParams['axes.grid'])

        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)
```
