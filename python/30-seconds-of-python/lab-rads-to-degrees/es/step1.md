# Radianes a Grados

Escribe una función de Python llamada `rads_to_degrees` que tome un solo argumento `rad`, que es un número de punto flotante que representa un ángulo en radianes. La función debe devolver el ángulo en grados como un número de punto flotante. Puedes utilizar la siguiente fórmula para convertir un ángulo de radianes a grados:

```
grados = radianes * (180 / pi)
```

donde `pi` es un valor constante que representa la relación entre la circunferencia de un círculo y su diámetro, que es aproximadamente igual a 3.14159.

Tu función debe importar la constante `pi` del módulo `math`.

```python
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```python
from math import pi

rads_to_degrees(pi / 2) # 90.0
```
