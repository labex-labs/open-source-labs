# Subsecuencia Crescente Más Larga

## Problema

Dada una secuencia de enteros, encontrar la subsecuencia creciente más larga. La subsecuencia puede no ser contigua y puede contener duplicados. Si hay múltiples soluciones, devolver cualquiera de ellas.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- ¿Es posible que haya duplicados?
  - Sí
- ¿Podemos suponer que las entradas son enteros?
  - Sí
- ¿Podemos suponer que las entradas son válidas?
  - No, debemos manejar entradas no válidas.
- ¿Esperamos que el resultado sea una matriz de la subsecuencia creciente más larga?
  - Sí
- ¿Podemos suponer que esto cabe en memoria?
  - Sí

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo se puede utilizar esta función:

- Ninguno -> Excepción
- [] -> []
- [3, 4, -1, 0, 6, 2, 3] -> [-1, 0, 2, 3]
