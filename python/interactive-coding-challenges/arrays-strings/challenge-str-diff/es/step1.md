# Diferencia entre cadenas

## Problema

Dadas dos cadenas, debemos encontrar el único carácter diferente entre ellas. Se asume que las cadenas son ASCII y están en minúsculas. No podemos suponer que las entradas son válidas, por lo que debemos comprobar si son None. Si las entradas son válidas, podemos suponer que solo hay un único carácter diferente entre las dos cadenas. También debemos asegurarnos de que la solución quepa en memoria.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- Las cadenas son ASCII.
- Las cadenas están en minúsculas.
- Debemos comprobar si la entrada es None.
- Solo hay un único carácter diferente entre las dos cadenas.
- La solución debe caber en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo usar la función:

- Entrada None -> TypeError
- 'ab', 'aab' -> 'a'
- 'aab', 'ab' -> 'a'
- 'abcd', 'abcde' -> 'e'
- 'aaabbcdd', 'abdbacade' -> 'e'
