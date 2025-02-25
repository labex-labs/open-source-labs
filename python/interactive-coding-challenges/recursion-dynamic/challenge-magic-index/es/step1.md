# Índice Mágico

## Problema

Dada una matriz ordenada de enteros con posibles duplicados, escribe una función de Python para encontrar el índice mágico, si existe, en la matriz. Si hay múltiples valores mágicos, devuelve el más a la izquierda. Si no hay ningún índice mágico, devuelve -1.

## Requisitos

Para resolver el problema, deben cumplirse los siguientes requisitos:

- La matriz está ordenada.
- Los elementos de la matriz no necesariamente son distintos.
- Los valores negativos están permitidos en la matriz.
- Si no hay ningún índice mágico, devuelve -1.

## Uso de Ejemplo

Los siguientes ejemplos ilustran el uso de la función:

- Entrada nula -> -1
- Matriz vacía -> -1

```txt
a[i]  -4 -2  2  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Resultado: 2

```txt
a[i]  -4 -2  1  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Resultado: 6

```txt
a[i]  -4 -2  1  6  6  6  7 10
  i    0  1  2  3  4  5  6  7
```

Resultado: -1
