# Multiplicación de matrices

## Problema

Dada una lista de matrices de 2x2, necesitamos encontrar el costo mínimo de multiplicarlas entre sí. El costo de multiplicar dos matrices es el número de multiplicaciones escalares requeridas. Por ejemplo, si tenemos las matrices A, B y C, y queremos calcular el producto ABC, el costo sería el número de multiplicaciones escalares necesarias para calcular cada elemento de la matriz resultante.

Para resolver este problema, necesitamos encontrar el orden óptimo de multiplicar las matrices. El orden en que multiplicamos las matrices afecta el costo total de la multiplicación. Por ejemplo, si tenemos las matrices A, B y C, y queremos calcular el producto ABC, podemos calcular (AB)C o A(BC). El costo de estas dos computaciones puede ser diferente, y necesitamos encontrar el orden óptimo que minimice el costo.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- Solo necesitamos calcular el costo de la multiplicación de matrices y no listar el orden real de las operaciones.
- No podemos asumir que las entradas son válidas y debemos manejar entradas no válidas.
- Podemos asumir que el problema cabe en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debe comportarse la función:

- `None` -> `Excepción`
- `[]` -> `0`
- `[Matrix(2, 3), Matrix(3, 6), Matrix(6, 4), Matrix(4, 5)]` -> `124`
