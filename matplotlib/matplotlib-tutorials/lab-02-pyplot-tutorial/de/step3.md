# Plotten mehrerer Linien

Wir können auch in einem Funktionsaufruf mehrere Linien mit unterschiedlichen Stilen mithilfe von Arrays plotten. Plotten wir drei Linien: eine gestrichelte rote Linie, blaue Quadrate und grüne Dreiecke:

```python
import numpy as np

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

Erklärung:

- Wir verwenden das `numpy`-Modul, um ein Array `t` mit gleichmäßig abgetasteten Zeitwerten zu erstellen.
- Die `plot`-Funktion wird mit drei Paaren von `x`- und `y`-Werten aufgerufen, gefolgt von den Formatzeichenfolgen `'r--'` (gestrichelte rote Linie), `'bs'` (blaue Quadrate) und `'g^'` (grüne Dreiecke).
