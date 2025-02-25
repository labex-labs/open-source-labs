# Grad in Radiant

Schreiben Sie eine Funktion `degrees_to_rads(deg)`, die einen Winkel in Grad als Argument nimmt und den Winkel in Radiant zurückgibt. Ihre Funktion sollte die folgende Formel verwenden, um Grad in Radiant umzurechnen:

```
radians = (degrees * pi) / 180.0
```

wobei `pi` ein konstanter Wert ist, der das Verhältnis der Kreisumfangs zu seinem Durchmesser darstellt (ungefähr 3,14159).

Ihre Funktion sollte den Winkel in Radiant auf 4 Nachkommastellen gerundet zurückgeben.

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```
