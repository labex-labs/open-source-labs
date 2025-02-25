# Radiant in Grad

Schreiben Sie eine Python-Funktion namens `rads_to_degrees`, die ein einzelnes Argument `rad` annimmt, das eine Gleitkommazahl ist, die einen Winkel in Radiant darstellt. Die Funktion sollte den Winkel in Grad als Gleitkommazahl zurückgeben. Sie können die folgende Formel verwenden, um einen Winkel von Radiant in Grad umzurechnen:

```
Grad = Radiant * (180 / Pi)
```

wobei `Pi` ein konstanter Wert ist, der das Verhältnis der Kreisumfangs zu seinem Durchmesser darstellt und ungefähr 3,14159 entspricht.

Ihre Funktion sollte die Konstante `Pi` aus dem Modul `math` importieren.

```python
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```python
from math import pi

rads_to_degrees(pi / 2) # 90.0
```
