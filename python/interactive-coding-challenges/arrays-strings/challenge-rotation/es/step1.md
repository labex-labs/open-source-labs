# Rotación

## Problema

Dadas dos cadenas s1 y s2, determinar si s1 es una rotación de s2 llamando (sólo una vez) a una función is_substring. La función is_substring toma dos cadenas como entrada y devuelve True si la primera cadena es una subcadena de la segunda cadena, y False en caso contrario.

## Requisitos

Para resolver este problema, debemos cumplir con los siguientes requisitos:

- La cadena es ASCII.
- La comparación es sensible a mayúsculas y minúsculas.
- Podemos utilizar estructuras de datos adicionales.
- Las cadenas caben en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debe comportarse la función:

- Si las cadenas tienen tamaños diferentes, la función debe devolver False.
- Si cualquiera de las cadenas es None, la función debe devolver False.
- Si una de las cadenas es un espacio y la otra no, la función debe devolver False.
- Si ambas cadenas son espacios, la función debe devolver True.
- Si s1 es una rotación de s2, la función debe devolver True.
