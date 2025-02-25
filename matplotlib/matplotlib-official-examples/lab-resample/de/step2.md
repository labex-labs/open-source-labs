# Die Klasse definieren

Wir werden eine Klasse `DataDisplayDownsampler` definieren, die die Daten aufniederschlüsselt und beim Zoomen neu berechnet. Der Konstruktor der Klasse wird die xdata und ydata als Eingabeparameter entgegennehmen. Wir werden die maximale Anzahl von Punkten auf 50 setzen und die Differenz von xdata berechnen.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
