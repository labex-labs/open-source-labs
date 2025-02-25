# Conversión de RGB a Hexadecimal

Escribe una función `rgb_to_hex(r, g, b)` que tome tres enteros que representen los valores de los componentes rojo, verde y azul de un color, y devuelva una cadena que represente el código de color hexadecimal. La cadena de salida debe estar en el formato `RRGGBB`, donde `RR`, `GG` y `BB` son valores hexadecimales de dos dígitos que representan los componentes rojo, verde y azul respectivamente.

Por ejemplo, si los valores de entrada son `255`, `165` y `1`, la salida debe ser la cadena `'FFA501'`.

```python
def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)
```

```python
rgb_to_hex(255, 165, 1) # 'FFA501'
```
