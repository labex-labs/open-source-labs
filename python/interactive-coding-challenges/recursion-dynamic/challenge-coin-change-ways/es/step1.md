# Maneras de dar cambio con monedas

## Problema

Dado un entero `n` y una matriz de monedas distintas, escribe una función para contar el número de maneras de dar cambio para `n` utilizando las monedas de la matriz. Una moneda se puede utilizar cualquier número de veces, y estamos contando combinaciones únicas.

Por ejemplo, si `n = 4` y `monedas = [1, 2]`, hay 3 maneras de dar cambio: 1+1+1+1, 1+2+1 y 2+2.

## Requisitos

Para resolver este problema, necesitarás:

- Escribir una función que tome dos argumentos: un entero `n` y una matriz de monedas distintas.
- Utilizar programación dinámica para contar el número de maneras de dar cambio para `n` utilizando las monedas de la matriz.
- Devolver el número de combinaciones únicas.

## Ejemplo

Entrada: `n = 4`, `monedas = [1, 2]`

Salida: 3. 1+1+1+1, 1+2+1, 2+2, serían las maneras de dar cambio.
