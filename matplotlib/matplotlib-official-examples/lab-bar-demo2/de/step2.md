# Daten für das Balkendiagramm erstellen

In diesem Schritt müssen wir Daten für das Balkendiagramm erstellen. Wir werden die numpy-Bibliothek verwenden, um ein Array von Werten zu erstellen, das wir für das Balkendiagramm verwenden werden.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
