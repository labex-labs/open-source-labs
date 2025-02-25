# Comprimir Alt

## Problema

Dada una cadena de texto, comprimirla de manera que las ocurrencias consecutivas del mismo carácter se reemplacen por ese carácter seguido del número de ocurrencias. Por ejemplo, la cadena 'AAABCCDDDD' se convertirá en 'A3BCCD4'. Sin embargo, si la cadena comprimida no es más corta que la cadena original, se devuelve la cadena original.

## Requisitos

Para resolver este desafío, deben cumplirse los siguientes requisitos:

- Se asume que la cadena es ASCII.
- La compresión es sensible a mayúsculas y minúsculas.
- Se pueden utilizar estructuras de datos adicionales.
- Se asume que la cadena cabe en memoria.

## Uso de ejemplo

Los siguientes son ejemplos de cómo se puede utilizar esta función:

- `compress(None)` devuelve `None`
- `compress('')` devuelve `''`
- `compress('AABBCC')` devuelve `'AABBCC'`
- `compress('AAABCCDDDD')` devuelve `'A3BCCD4'`
