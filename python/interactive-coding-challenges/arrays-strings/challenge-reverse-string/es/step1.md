# Invertir una cadena

## Problema

Implementar una función para invertir una cadena (una lista de caracteres) en el mismo lugar. Esto significa que la función debe modificar la cadena original en lugar de crear una nueva. La función debe tomar una lista de caracteres como entrada y devolver la misma lista con los caracteres invertidos.

Para resolver este problema, debemos considerar algunos requisitos:

## Requisitos

- Se puede suponer que la cadena es ASCII.
- Dado que debemos hacerlo en el mismo lugar, no podemos usar el operador de rebanado ni la función `reversed`.
- Dado que las cadenas de Python son inmutables, podemos usar una lista de caracteres en su lugar.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debe comportarse la función:

- `None` -> `None`
- `['']` -> `['']`
- `['f', 'o', 'o','', 'b', 'a', 'r']` -> `['r', 'a', 'b','', 'o', 'o', 'f']`
