# Cambio de monedas mínimo

## Problema

Dado un conjunto de monedas con denominaciones menores a n centavos, necesitamos determinar el número mínimo de maneras de obtener n centavos utilizando estas monedas. Las monedas se pueden utilizar en cualquier combinación y tenemos un número ilimitado de monedas de cada denominación. No necesitamos reportar la combinación(es) de monedas que representen el mínimo.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- Las monedas deben alcanzar exactamente n centavos.
- Podemos asumir que tenemos un número ilimitado de monedas para obtener n centavos.
- No necesitamos reportar la combinación(es) de monedas que representen el mínimo.
- No podemos asumir que las denominaciones de las monedas estén dadas en orden ascendente.
- Podemos asumir que esto cabe en memoria.

## Uso de ejemplo

Aquí hay algunos ejemplos de cómo se puede utilizar esta función:

- monedas: Ninguna o n: Ninguna -> Excepción
- monedas: [] o n: 0 -> 0
- monedas: [1, 2, 3] o [3, 2, 1] -> 2
