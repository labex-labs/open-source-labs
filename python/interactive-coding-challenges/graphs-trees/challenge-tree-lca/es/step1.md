# Árbol Lca

## Problema

Dado un árbol binario y dos nodos, encontrar su ancestro común más bajo.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- El árbol dado es un árbol binario, no un árbol de búsqueda binaria.
- No podemos suponer que los dos nodos ya estén en el árbol.
- Podemos suponer que el árbol binario cabe en memoria.

## Uso de ejemplo

Considere el siguiente árbol binario:

```txt
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
```

Podemos probar nuestra función con las siguientes entradas y salidas esperadas:

- 0, 5 -> Ninguno (ninguno de los dos nodos está en el árbol)
- 5, 0 -> Ninguno (ninguno de los dos nodos está en el árbol)
- 1, 8 -> 3
- 12, 8 -> 5
- 12, 40 -> 10
- 9, 20 -> 9
- 3, 5 -> 5
