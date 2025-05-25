# Criar Classe GeoAxes

Criaremos uma classe base abstrata para projeções geográficas chamada `GeoAxes`.

```python
class GeoAxes(Axes):
    """
    Uma classe base abstrata para projeções geográficas
    """

    class ThetaFormatter(Formatter):
        """
        Usado para formatar os rótulos de marcação theta. Converte a unidade nativa
        de radianos em graus e adiciona um símbolo de grau.
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
        # Não registrar xaxis ou yaxis com spines -- como feito em
        # Axes._init_axis() -- até que GeoAxes.xaxis.clear() funcione.
        # self.spines['geo'].register_axis(self.yaxis)

    def clear(self):
        # docstring herdado
        super().clear()

        self.set_longitude_grid(30)
        self.set_latitude_grid(15)
        self.set_longitude_grid_ends(75)
        self.xaxis.set_minor_locator(NullLocator())
        self.yaxis.set_minor_locator(NullLocator())
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')
        self.yaxis.set_tick_params(label1On=True)
        # Por que precisamos ativar os rótulos de marcação yaxis, mas
        # os rótulos de marcação xaxis já estão ativados?

        self.grid(rcParams['axes.grid'])

        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)
```
