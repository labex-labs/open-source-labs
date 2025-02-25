# Buscar en una matriz ordenada

## Problema

Dada una matriz ordenada, debemos buscar un elemento específico en ella. La matriz está ordenada de manera que los elementos en cada fila y columna están ordenados en orden ascendente. La matriz no necesariamente es una matriz cuadrada. Debemos devolver la posición del elemento en la matriz como una tupla (fila, columna) si se encuentra, de lo contrario, debemos devolver None.

## Requisitos

Para resolver este problema, debemos hacer los siguientes supuestos:

- Los elementos en cada fila de la matriz están ordenados en orden ascendente.
- Los elementos en cada columna de la matriz están ordenados en orden ascendente.
- La matriz no es irregular, es decir, es un rectángulo.
- El orden de clasificación es ascendente.
- La matriz no necesariamente es una matriz cuadrada.
- La salida es una tupla (fila, columna).
- El elemento que estamos buscando puede o no estar en la matriz.
- Las entradas pueden o no ser válidas.
- La solución debe caber en la memoria.

## Uso de ejemplo

Podemos utilizar los siguientes casos de prueba para verificar nuestra solución:

- Si la entrada es None, la función debe generar una excepción.
- Si el elemento se encuentra en la matriz, la función debe devolver su posición como una tupla (fila, columna).
- Si el elemento no se encuentra en la matriz, la función debe devolver None.
