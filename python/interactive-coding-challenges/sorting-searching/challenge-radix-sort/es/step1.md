# Método de clasificación Radix

## Problema

Implementar el algoritmo de clasificación Radix para ordenar una lista de enteros. El algoritmo ordena los enteros comparando sus dígitos, comenzando por el dígito menos significativo hasta el más significativo. El algoritmo primero ordena los enteros basados en el dígito menos significativo, luego el segundo dígito menos significativo, y así sucesivamente hasta que el dígito más significativo está ordenado.

## Requisitos

Para implementar el método de clasificación Radix, deben cumplirse los siguientes requisitos:

- La entrada debe ser una lista de enteros.
- Verificar si hay None en lugar de una matriz.
- Asumir que los elementos de la matriz son enteros.
- Los dígitos deben ser de base 10.
- El algoritmo debe ser capaz de manejar cualquier número de dígitos.
- El algoritmo debe caber en memoria.

## Uso de ejemplo

Los siguientes son ejemplos de cómo utilizar el algoritmo de clasificación Radix:

- None -> Excepción
- [] -> []
- [128, 256, 164, 8, 2, 148, 212, 242, 244] -> [2, 8, 128, 148, 164, 212, 242, 244, 256]
