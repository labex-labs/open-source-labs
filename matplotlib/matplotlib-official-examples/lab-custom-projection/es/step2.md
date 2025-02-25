# Crear la clase GeoAxes

Crearemos una clase base abstracta para proyecciones geográficas llamada `GeoAxes`.

```python
class GeoAxes(Axes):
    """
    Una clase base abstracta para proyecciones geográficas
    """

    class ThetaFormatter(Formatter):
        """
        Se utiliza para formatear las etiquetas de los ticks de theta. Convierte la unidad nativa de radianes a grados y agrega un símbolo de grado.
        """
        def __init__(self, round_to=1.0):
            self._round_to = round_to

        def __call__(self, x, pos=None):
            grados = round(np.rad2deg(x) / self._round_to) * self._round_to
            return f"{grados:0.0f}\N{DEGREE SIGN}"

    RESOLUTION = 75

    def _init_axis(self):
        self.xaxis = maxis.XAxis(self)
        self.yaxis = maxis.YAxis(self)
        # No registre xaxis o yaxis con spines -- como se hace en
        # Axes._init_axis() -- hasta que GeoAxes.xaxis.clear() funcione.
        # self.spines['geo'].register_axis(self.yaxis)

    def clear(self):
        # docstring heredado
        super().clear()

        self.set_longitude_grid(30)
        self.set_latitude_grid(15)
        self.set_longitude_grid_ends(75)
        self.xaxis.set_minor_locator(NullLocator())
        self.yaxis.set_minor_locator(NullLocator())
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')
        self.yaxis.set_tick_params(label1On=True)
        # ¿Por qué necesitamos encender las etiquetas de los ticks del eje y, pero
        # las etiquetas de los ticks del eje x ya están encendidas?

        self.grid(rcParams['axes.grid'])

        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)
```
