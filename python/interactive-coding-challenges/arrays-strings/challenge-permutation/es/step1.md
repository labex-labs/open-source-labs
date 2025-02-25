# Permutación

## Problema

Dadas dos cadenas, debemos determinar si una cadena es una permutación de la otra. Una permutación se define como un reordenamiento de los caracteres en una cadena. Por ejemplo, "act" es una permutación de "cat".

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La cadena es ASCII.
- El espacio en blanco es importante.
- La comparación es sensible a mayúsculas y minúsculas. Por ejemplo, "Nib" y "bin" no son una coincidencia.
- Podemos utilizar estructuras de datos adicionales.
- Podemos suponer que las cadenas caben en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo se puede utilizar esta función:

- Uno o más entradas None -> False
- Una o más cadenas vacías -> False
- 'Nib', 'bin' -> False
- 'act', 'cat' -> True
- 'a ct', 'ca t' -> True
