# N Elementos Mínimos

## Problema

Escribe una función llamada `min_n(lst, n = 1)` que tome una lista `lst` y un entero opcional `n` (valor predeterminado de `1`). La función debe devolver una nueva lista que contenga los `n` elementos más pequeños de la lista original `lst`. Si no se proporciona `n`, la función debe devolver una lista que contenga el elemento más pequeño de `lst`.

Si `n` es mayor o igual que la longitud de `lst`, la función debe devolver la lista original ordenada en orden ascendente.

Tu función debe cumplir con estos pasos:

1. Utiliza la función integrada `sorted()` para ordenar la lista en orden ascendente.
2. Utiliza la notación de rebanado para obtener el número especificado de elementos.
3. Devuelve la lista resultante.

## Ejemplo

```python
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
```
