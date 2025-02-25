# Radiant in Grad Herausforderung

## Problem

Schreiben Sie eine Python-Funktion namens `rads_to_degrees`, die ein einzelnes Argument `rad` annimmt, das eine Gleitkommazahl ist, die einen Winkel in Radiant darstellt. Die Funktion sollte den Winkel in Grad als Gleitkommazahl zurückgeben. Sie können die folgende Formel verwenden, um einen Winkel von Radiant in Grad umzurechnen:

```
Grad = Radiant * (180 / pi)
```

wobei `pi` ein konstanter Wert ist, der das Verhältnis der Kreisumfangs zu seinem Durchmesser darstellt und ungefähr 3,14159 entspricht.

Ihre Funktion sollte die Konstante `pi` aus dem Modul `math` importieren.

## Beispiel

Hier ist ein Beispiel, wie Ihre Funktion funktionieren sollte:

```python
from math import pi

assert rads_to_degrees(pi / 2) == 90.0
```
