# Potencia de dos

## Problema

Escribe una función de Python llamada `is_power_of_two` que tome un entero como parámetro y devuelva `True` si la entrada es una potencia de dos, y `False` en caso contrario. Una potencia de dos es cualquier número que se puede expresar como 2^n, donde n es un entero. Por ejemplo, 2, 4, 8 y 16 son todas potencias de dos.

## Requisitos

La función `is_power_of_two` debe cumplir con los siguientes requisitos:

- El número de entrada debe ser un entero.
- La función debe manejar las entradas no válidas de manera adecuada.
- La salida debe ser un booleano.
- La función debe ajustarse a las restricciones de memoria.

## Uso de ejemplo

Aquí hay algunos ejemplos de cómo debe comportarse la función `is_power_of_two`:

- `is_power_of_two(None)` debe generar un `TypeError`.
- `is_power_of_two(0)` debe devolver `False`.
- `is_power_of_two(1)` debe devolver `True`.
- `is_power_of_two(2)` debe devolver `True`.
- `is_power_of_two(15)` debe devolver `False`.
- `is_power_of_two(16)` debe devolver `True`.
