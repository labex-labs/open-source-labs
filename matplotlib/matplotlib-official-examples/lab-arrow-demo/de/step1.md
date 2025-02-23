# Bibliotheken importieren und die Funktion definieren

Der erste Schritt besteht darin, die erforderlichen Bibliotheken zu importieren und die Funktion `make_arrow_graph()` zu definieren. Diese Funktion nimmt verschiedene Parameter wie die Achsen, die Daten, die Größe, die Anzeige, die Form, die maximale Pfeilbreite, den Pfeilabstand, Alpha, die Normalisierung der Daten, die Kantenfarbe, die Labelfarbe und die zusätzlichen Schlüsselwortargumente entgegen. Sie verwendet diese Parameter, um ein Pfeildiagramm zu erstellen.

```python
# Import libraries
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def make_arrow_graph(ax, data, size=4, display='length', shape='right',
                     max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5,
                     normalize_data=False, ec=None, labelcolor=None,
                     **kwargs):
    """
    Erstellt ein Pfeildiagramm.

    Parameter
    ----------
    ax
        Die Achsen, auf denen das Diagramm gezeichnet wird.
    data
        Dictionary mit Wahrscheinlichkeiten für die Basen und Paarübergänge.
    size
        Größe des Diagramms in Zoll.
    display : {'length', 'width', 'alpha'}
        Die zu ändernde Pfeileigenschaft.
    shape : {'full', 'left', 'right'}
        Für volle oder halbe Pfeile.
    max_arrow_width : float
        Maximale Breite eines Pfeils in Datenkoordinaten.
    arrow_sep : float
        Abstand zwischen den Pfeilen in einem Paar in Datenkoordinaten.
    alpha : float
        Maximale Deckkraft der Pfeile.
    **kwargs
        `.FancyArrow`-Eigenschaften, z.B. *linewidth* oder *edgecolor*.
    """

    # code block
```
