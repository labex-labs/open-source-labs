# Conversión de hexadecimal a RGB

## Problema

Escribe una función `hex_to_rgb(hex_code)` que tome un código de color hexadecimal como una cadena y devuelva una tupla de enteros correspondientes a sus componentes RGB. La función debe realizar los siguientes pasos:

1. Utiliza una comprensión de listas en combinación con `int()` y la notación de rebanado de listas para obtener los componentes RGB de la cadena hexadecimal.
2. Utiliza `tuple()` para convertir la lista resultante en una tupla.

## Ejemplo

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
