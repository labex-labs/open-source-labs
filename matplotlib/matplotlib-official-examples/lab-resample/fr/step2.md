# Définition de la classe

Nous allons définir une classe `DataDisplayDownsampler` qui réduira l'échantillonnage des données et recomputera lorsque le zoom est effectué. Le constructeur de la classe prendra les données x et y comme paramètres d'entrée. Nous définirons le nombre maximum de points à 50 et calculerons le delta des données x.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
