# Subsecuencia Común Más Larga

## Problema

Dadas dos cadenas, encontrar la subsecuencia común más larga. Una subsecuencia es una secuencia que se puede derivar de otra secuencia eliminando algunos o ningún elemento sin cambiar el orden de los elementos restantes. Por ejemplo, "ACE" es una subsecuencia de "ABCDE" pero no de "AEDCA".

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- Las entradas pueden no ser válidas, por lo que el programa debe manejar entradas no válidas.
- Las cadenas son ASCII.
- El programa debe ser sensible a mayúsculas y minúsculas.
- Una subsecuencia es un bloque no contiguo de caracteres.
- El programa debe devolver una cadena como resultado.
- El programa debe asumir que cabe en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debe comportarse el programa:

- Si str0 o str1 es None, se debe generar una excepción.
- Si str0 o str1 es igual a 0, se debe devolver una cadena vacía.
- Caso general:

```
str0 = 'ABCDEFGHIJ'
str1 = 'FOOBCDBCDE'

resultado: 'BCDE'
```
