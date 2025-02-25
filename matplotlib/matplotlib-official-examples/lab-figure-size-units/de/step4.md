# Figurengröße in Pixeln

Wir können auch die Figurengröße in Pixeln angeben. Dazu müssen wir den Pixelwert in Zoll umrechnen. Wir können den Umrechnungsfaktor von Pixeln in Zoll erhalten, indem wir 1 durch den dpi-Wert (Dots per Inch) dividieren. Wir können diesen Wert dann als figsize-Parameter in der subplots-Funktion verwenden. Der folgende Code zeigt, wie man eine Figur mit einer Größe von 600 Pixeln x 200 Pixeln erstellt.

```python
px = 1/plt.rcParams['figure.dpi']  # Pixel in Zoll
plt.subplots(figsize=(600*px, 200*px))
plt.show()
```
