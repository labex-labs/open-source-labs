# `from` Modul importieren

Dies wählt ausgewählte Symbole aus einem Modul aus und macht sie lokal verfügbar.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

Dadurch können Teile eines Moduls verwendet werden, ohne dass der Modulprefix eingegeben werden muss. Dies ist für häufige Namen nützlich.
