# Conversión de hexadecimal a RGB

Escribe una función `hex_to_rgb(hex_code)` que tome un código de color hexadecimal como una cadena y devuelva una tupla de enteros correspondientes a sus componentes RGB. La función debe realizar los siguientes pasos:

1. Utiliza una comprensión de lista en combinación con `int()` y la notación de rebanado de lista para obtener los componentes RGB de la cadena hexadecimal.
2. Utiliza `tuple()` para convertir la lista resultante en una tupla.

```python
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
