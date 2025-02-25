# Dibuja línea

## Problema

Implementa el método `draw_line(screen, width, x1, x2)` donde `screen` es una lista de bytes, `width` es divisible por 8 y `x1`, `x2` son posiciones absolutas de píxeles. El método debe establecer los bits correspondientes en `screen` para dibujar una línea de `x1` a `x2`.

### Requisitos

La implementación de `draw_line` debe cumplir con los siguientes requisitos:

- No se puede asumir que las entradas son válidas.
- Los bits correspondientes en `screen` deben ser establecidos para dibujar la línea.
- Se puede asumir que la implementación cabe en memoria.

## Uso de ejemplo

Los siguientes ejemplos ilustran el comportamiento esperado de `draw_line`:

- Entradas no válidas -> Excepción
  - `screen` está vacía
  - `width` = 0
  - cualquier parámetro de entrada es `None`
  - `x1` o `x2` está fuera de los límites
- Caso general para `len(screen)` = 20, `width` = 32:
  - `x1` = 2, `x2` = 6
    - `screen[0]` = `int('00111110', base=2)`
  - `x1` = 68, `x2` = 80
    - `screen[8]`, `int('00001111', base=2)`
    - `screen[9]`, `int('11111111', base=2)`
    - `screen[10]`, `int('10000000', base=2)`
