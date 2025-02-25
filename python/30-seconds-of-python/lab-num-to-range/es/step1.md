# Mapear un número a un rango

Escribe una función llamada `num_to_range` que tome cinco argumentos: `num`, `inMin`, `inMax`, `outMin` y `outMax`. La función debe devolver `num` mapeado entre `outMin` - `outMax` a partir de `inMin` - `inMax`. En otras palabras, la función debe tomar un número (`num`) que se encuentra dentro de un cierto rango (`inMin` - `inMax`) y mapearlo a un nuevo rango (`outMin` - `outMax`).

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
