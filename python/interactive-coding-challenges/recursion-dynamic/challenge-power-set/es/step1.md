# Conjunto Potencia

## Problema

Dado un conjunto, devolver todos los subconjuntos posibles del conjunto. Los subconjuntos deben ser únicos, lo que significa que si dos subconjuntos tienen los mismos elementos, deben considerarse el mismo subconjunto. El conjunto vacío también debe incluirse como subconjunto. Las entradas no necesariamente son únicas y no podemos suponer que las entradas son válidas. Sin embargo, podemos suponer que el problema cabe en memoria.

## Requisitos

Para generar el conjunto potencia de un conjunto, debemos cumplir con los siguientes requisitos:

- Los subconjuntos resultantes deben ser únicos, considerando como iguales a los subconjuntos con los mismos elementos.
- El conjunto vacío debe incluirse como subconjunto.
- Las entradas no necesariamente son únicas.
- No podemos suponer que las entradas son válidas.
- Podemos suponer que el problema cabe en memoria.

## Uso de Ejemplo

```txt
* None -> None
* [] -> [[]]
* ['a'] -> [[],
            ['a']]
* ['a', 'b'] -> [[],
                 ['a'],
                 ['b'],
                 ['a', 'b']]
* ['a', 'b', 'c'] -> [[],
                      ['a'],
                      ['b'],
                      ['c'],
                      ['a', 'b'],
                      ['a', 'c'],
                      ['b', 'c'],
                      ['a', 'b', 'c']]
```
