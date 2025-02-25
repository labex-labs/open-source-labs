# Sumar una lista basada en una función

## Problema

Escribe una función `sum_by(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe asignar a cada elemento de la lista un valor usando la función proporcionada y devolver la suma de los valores.

## Ejemplo

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```

En el ejemplo anterior, la función `sum_by()` toma una lista de diccionarios y una función lambda que extrae el valor de la clave `'n'` de cada diccionario. La función asigna a cada diccionario su valor de `'n'` y devuelve la suma de los valores, que es `20`.
