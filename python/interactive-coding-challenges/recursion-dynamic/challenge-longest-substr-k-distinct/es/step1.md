# Subcadena más larga con k caracteres distintos

## Problema

Dada una cadena y un entero k, encontrar la longitud de la subcadena más larga que contiene como máximo k caracteres distintos. Una subcadena es un bloque contiguo de caracteres. Por ejemplo, en la cadena "abcabcdefgghiij", la subcadena más larga con como máximo 3 caracteres distintos es "abcabc". Si hay múltiples subcadenas con la misma longitud, devolver cualquiera de ellas.

## Requisitos

Para resolver este desafío, deben cumplirse los siguientes requisitos:

- Las entradas pueden no ser válidas, por lo que el código debe manejar las entradas no válidas de manera adecuada.
- Las cadenas son ASCII.
- La búsqueda es sensible a mayúsculas y minúsculas.
- Una subcadena es un bloque contiguo de caracteres.
- El resultado debe ser un entero.
- El código debe ser capaz de manejar la entrada dentro de los límites de memoria.

## Uso de ejemplo

Los siguientes ejemplos demuestran el comportamiento esperado del código:

- Ninguno -> TypeError
- '', k = 3 -> 0
- 'abcabcdefgghiij', k=3 -> 6
- 'abcabcdefgghighij', k=3 -> 7
