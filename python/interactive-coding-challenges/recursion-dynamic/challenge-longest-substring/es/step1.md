# Subcadena más larga

## Problema

Dadas dos cadenas, la tarea es encontrar la subcadena común más larga. Una subcadena es un bloque contiguo de caracteres. La solución debe ser sensible a mayúsculas y minúsculas y se asume que las cadenas son ASCII. La salida debe ser una cadena y el programa debe asumir que las entradas no son necesariamente válidas. Sin embargo, puede asumir que el problema cabe en memoria.

## Requisitos

Para resolver este problema, el programa debe cumplir con los siguientes requisitos:

- Las entradas no son necesariamente válidas.
- Las cadenas son ASCII.
- La solución debe ser sensible a mayúsculas y minúsculas.
- Una subcadena es un bloque contiguo de caracteres.
- La salida debe ser una cadena.
- El programa debe asumir que el problema cabe en memoria.

## Uso de ejemplo

El programa debe comportarse de la siguiente manera:

- Si str0 o str1 es None, se debe generar una excepción.
- Si str0 o str1 es igual a 0, la salida debe ser una cadena vacía.
- En el caso general, dado str0 = 'ABCDEFGHIJ' y str1 = 'FOOBCDBCDE', la salida debe ser 'BCDE'.
