# Encuentra el valor mínimo de una lista basado en una función

## Problema

Escribe una función llamada `min_by(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe mapear cada elemento de la lista a un valor utilizando la función proporcionada y luego devolver el valor mínimo.

## Ejemplo

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```

En el ejemplo anterior, la función `min_by()` se llama con una lista de diccionarios y una función lambda que extrae el valor de la clave `'n'` de cada diccionario. La función devuelve el valor mínimo de la lista, que es `2`.
