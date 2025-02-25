# Generar números primos

## Problema

Escribe una función de Python que genere una lista de números primos. La función debe tomar un entero como entrada y devolver una lista de valores booleanos, donde cada valor corresponde a si el índice es un número primo o no. Por ejemplo, si la entrada es 20, la salida debe ser [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True], donde el valor en el índice 2 es True porque 2 es un número primo, y el valor en el índice 4 es False porque 4 no es un número primo.

## Requisitos

- La función no debe considerar 1 como un número primo.
- La función debe manejar entradas no válidas elevando una excepción.
- La función debe generar la lista de números primos en memoria.

## Uso de ejemplo

- Ninguno -> Excepción
- No es un int -> Excepción
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
