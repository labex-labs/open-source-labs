# Contar Elementos Agrupados

## Problema

Escribe una función `count_by(lst, fn = lambda x: x)` que tome una lista `lst` y una función `fn` como argumentos. La función debe agrupar los elementos de la lista en función de la función dada y devolver un diccionario con la cuenta de elementos en cada grupo.

Para resolver este problema, puedes seguir estos pasos:

1. Inicializa un diccionario usando `collections.defaultdict`.
2. Utiliza `map()` para aplicar la función dada a cada elemento de la lista.
3. Itera sobre los valores mapeados e incrementa la cuenta de cada elemento en el diccionario.

La función debe devolver el diccionario resultante.

## Ejemplo

```python
count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```

En el primer ejemplo, la función `floor` se utiliza para agrupar los elementos de la lista `[6.1, 4.2, 6.3]`. El diccionario resultante tiene dos claves: `6` y `4`, con valores `2` y `1`, respectivamente.

En el segundo ejemplo, la función `len` se utiliza para agrupar los elementos de la lista `['one', 'two', 'three']`. El diccionario resultante tiene dos claves: `3` y `5`, con valores `2` y `1`, respectivamente.
