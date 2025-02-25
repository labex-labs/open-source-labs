# Permutaciones

## Problema

Dada una cadena de entrada, la tarea es encontrar todas las permutaciones posibles de los caracteres en la cadena. La salida debe ser una lista de cadenas, donde cada cadena representa una permutación única de la cadena de entrada. La cadena de entrada puede contener duplicados, pero la salida no debe tener ningún duplicado.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La entrada puede contener duplicados.
- La salida no debe tener ningún duplicado.
- La salida debe ser una lista de cadenas.
- Los resultados no necesitan estar ordenados.
- Las entradas no siempre pueden ser válidas.
- La solución debe caber en memoria.

## Uso de ejemplo

A continuación, se presentan algunos ejemplos de cómo debe comportarse la función:

- Si la entrada es None, la salida debe ser None.
- Si la entrada es una cadena vacía, la salida debe ser una cadena vacía.
- Si la entrada es 'AABC', la salida debe ser ['AABC', 'AACB', 'ABAC', 'ABCA', 'ACAB', 'ACBA', 'BAAC', 'BACA', 'BCAA', 'CAAB', 'CABA', 'CBAA'].
