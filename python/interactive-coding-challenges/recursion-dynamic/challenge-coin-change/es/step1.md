# Cambio de monedas

## Problema

Dado un conjunto de monedas de diferentes denominaciones y una cantidad total de dinero n, determinar el número total de maneras únicas de hacer cambio para n centavos. Las monedas proporcionadas tienen denominaciones menores que n centavos.

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- Las monedas deben alcanzar exactamente n centavos.
- Se puede asumir un número ilimitado de monedas para hacer n centavos.
- No es necesario reportar la combinación(s) de monedas que representen el mínimo.
- Las denominaciones de las monedas no se dan en orden ascendente.
- La solución debe caber en memoria.

## Uso de ejemplo

Los siguientes ejemplos demuestran el uso del problema de cambio de monedas:

- monedas: Ninguna o n: Ninguna -> Excepción
- monedas: [] o n: 0 -> 0
- monedas: [1, 2, 3], n: 5 -> 5
