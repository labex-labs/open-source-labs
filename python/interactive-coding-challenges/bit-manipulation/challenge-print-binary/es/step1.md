# Imprimir binario

## Problema

Escribe una función de Python que tome como entrada un número real entre 0 y 1 y devuelva su representación binaria como una cadena. Si la longitud de la representación es mayor que 32, devuelve 'ERROR'.

## Requisitos

Para resolver este problema, debemos garantizar los siguientes requisitos:

- La entrada debe ser un flotante.
- La salida debe ser una cadena.
- El rango de la entrada está entre 0 y 1, pero los valores 0 y 1 no están incluidos.
- El resultado debe incluir un cero final y un punto decimal.
- El cero inicial y el punto decimal se cuentan en el límite de 32 caracteres.
- No podemos suponer que las entradas son válidas.
- Podemos suponer que el programa cabe en memoria.

## Uso de ejemplo

Aquí hay algunos ejemplos de cómo debe comportarse la función:

- Ninguno -> 'ERROR'
- Fuera de los límites (0, 1) -> 'ERROR'
- 0.625 -> 0.101
- 0.987654321 -> 'ERROR'
