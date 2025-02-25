# Comprobar si un número es primo

## Problema

Escribe una función de Python que tome un entero como entrada y devuelva `True` si el número es primo, y `False` en caso contrario. Si la entrada no es un entero o es menor que 2, la función debe generar una excepción.

Un número se considera primo si solo es divisible por 1 y sí mismo. Por ejemplo, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97 son los primeros 25 números primos.

## Requisitos

El programa debe cumplir con los siguientes requisitos:

- La función debe tomar un entero como entrada.
- Si la entrada no es un entero o es menor que 2, la función debe generar una excepción.
- La función debe devolver `True` si la entrada es un número primo, y `False` en caso contrario.
- El programa no debe considerar 1 como un número primo.

## Uso de ejemplo

- `check_prime(None)` -> `Excepción`
- `check_prime('hello')` -> `Excepción`
- `check_prime(1)` -> `False`
- `check_prime(7)` -> `True`
