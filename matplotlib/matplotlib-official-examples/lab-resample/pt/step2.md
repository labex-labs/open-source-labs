# Definindo a classe

Definiremos uma classe `DataDisplayDownsampler` que fará o _downsample_ dos dados e recalculará quando houver zoom. O construtor da classe receberá `xdata` e `ydata` como parâmetros de entrada. Definiremos o número máximo de pontos como 50 e calcularemos o delta de `xdata`.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
