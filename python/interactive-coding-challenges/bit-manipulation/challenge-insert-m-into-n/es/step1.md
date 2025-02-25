# Insertar M en N

## Problema

Dados dos números de 16 bits, `n` y `m`, y dos índices `i` y `j`, insertar `m` en `n` de modo que `m` comience en el bit `j` y termine en el bit `i`. El programa debe manejar los siguientes casos:

- Si no se da ninguna como entrada, se debe generar una excepción.
- Si se da un índice negativo para `i` o `j`, se debe generar una excepción.
- Si las entradas son inválidas, se debe generar una excepción.
- Si `i` a través de `j` no tiene suficiente espacio para `m`, se debe generar una excepción.

El programa debe devolver el número de 16 bits resultante después de la inserción.

## Requisitos

El programa debe cumplir con los siguientes requisitos:

- `j` debe ser mayor que `i`.
- `i` a través de `j` debe tener suficiente espacio para `m`.
- Las entradas deben ser válidas.
- El programa debe caber en memoria.

## Uso de ejemplo

A continuación se muestra un ejemplo de uso del programa:

```txt
i      = 2
j      = 6
n      = 0000 0100 0000 0000
m      = 0000 0000 0001 0011
result = 0000 0100 0100 1100
```

En este ejemplo, `m` se inserta en `n` de modo que `m` comience en el bit `j = 6` y termine en el bit `i = 2`. El número de 16 bits resultante es `0000 0100 0100 1100`.
