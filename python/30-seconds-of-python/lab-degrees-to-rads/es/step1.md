# Grados a Radianes

Escribe una función `degrees_to_rads(deg)` que tome un ángulo en grados como argumento y devuelva el ángulo en radianes. Tu función debe utilizar la siguiente fórmula para convertir grados a radianes:

```
radians = (degrees * pi) / 180.0
```

donde `pi` es un valor constante que representa la razón entre la circunferencia de un círculo y su diámetro (aproximadamente 3.14159).

Tu función debe devolver el ángulo en radianes redondeado a 4 decimales.

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```
