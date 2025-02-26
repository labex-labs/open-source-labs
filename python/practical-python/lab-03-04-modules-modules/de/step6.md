# `import as`-Anweisung

Sie können den Namen eines Moduls ändern, wenn Sie es importieren:

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

Es funktioniert genauso wie ein normaler Import. Es benennt das Modul nur in dieser Datei um.
