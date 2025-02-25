# Desafío de Python: Escaleras

## Problema

Imagina que estás parado al pie de una escalera con n escalones. Puedes dar un paso, dos pasos o tres pasos a la vez. El problema es determinar cuántas maneras posibles hay de subir hasta el n-ésimo escalón.

Por ejemplo, si hay 3 escalones, puedes subir las escaleras de las siguientes maneras:

- 1-1-1
- 1-2
- 2-1
- 3

Entonces, hay 4 maneras posibles de subir hasta el 3er escalón.

## Requisitos

Para resolver este problema, debemos tener en cuenta los siguientes requisitos:

- Si n == 0, el resultado debe ser 1. Sin embargo, hay diferentes enfoques para este problema, que se pueden discutir.
- No podemos asumir que las entradas son válidas.
- Podemos asumir que el problema cabe en la memoria.

## Uso de ejemplo

A continuación, se presentan algunos ejemplos de cómo se puede resolver este problema utilizando Python:

- Entrada nula o negativa -> Excepción
- n == 0 -> 1
- n == 1 -> 1
- n == 2 -> 2
- n == 3 -> 4
- n == 4 -> 7
- n == 10 -> 274
