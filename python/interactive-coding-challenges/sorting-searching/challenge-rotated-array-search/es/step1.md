# Búsqueda en matriz rotada

## Problema

Dada una matriz ordenada que se ha rotado un número de veces, necesitamos encontrar un elemento específico en la matriz. Por ejemplo, si la matriz ordenada original era [1, 2, 3, 4, 5] y se rotó dos veces para convertirse en [3, 4, 5, 1, 2], necesitamos encontrar el índice de un elemento específico, como 4.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La entrada es una matriz de enteros.
- No sabemos cuántas veces se rotó la matriz.
- La matriz estaba originalmente ordenada en orden ascendente.
- Para la salida, debemos devolver el índice del elemento que estamos buscando.
- No podemos asumir que las entradas son válidas.
- Podemos asumir que la solución cabe en memoria.

## Uso de ejemplo

A continuación, se presentan algunos ejemplos de cómo se puede usar esta función:

- Si no se proporciona ninguna entrada, se debe generar una excepción.
- Si se proporciona una matriz vacía, se debe devolver None.
- Si el elemento que estamos buscando no se encuentra en la matriz, se debe devolver None.
- Si la matriz contiene duplicados, la función todavía debe ser capaz de encontrar el índice correcto.
- Si la matriz no contiene duplicados, la función todavía debe ser capaz de encontrar el índice correcto.
