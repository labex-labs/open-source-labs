# Operaciones matemáticas

## Problema

Crea una clase de Python con un método de inserción que pueda insertar un entero en una lista. La clase también debe admitir el cálculo del máximo, mínimo, promedio y moda de la lista con una complejidad de tiempo O(1). La clase debe manejar los siguientes casos:

- Si la entrada no es válida, debe generar un TypeError.
- Si la lista está vacía, debe generar un ValueError.
- Si hay múltiples modas, puede devolver cualquiera de las modas.

## Requisitos

Para resolver el problema anterior, debemos cumplir con los siguientes requisitos:

- Las entradas pueden no ser válidas, por lo que no podemos suponer que las entradas son válidas.
- El rango de las entradas está entre 0 y 100 inclusive.
- El promedio debe devolver un número de punto flotante.
- Los otros resultados deben devolver un entero.
- Si hay múltiples modas, la clase puede devolver cualquiera de las modas.
- Podemos suponer que la lista cabe en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo usar la clase:

- Ninguno -> TypeError
- [] -> ValueError
- [5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
  - máximo: 9
  - mínimo: 2
  - promedio: 4.909090909090909
  - moda: 9 o 2
