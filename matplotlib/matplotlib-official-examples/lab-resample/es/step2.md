# Definiendo la clase

Definiremos una clase `DataDisplayDownsampler` que reducirá la resolución de los datos y los recomputará cuando se amplíe. El constructor de la clase tomará los parámetros de entrada `xdata` e `ydata`. Estableceremos el número máximo de puntos en 50 y calcularemos el delta de `xdata`.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
