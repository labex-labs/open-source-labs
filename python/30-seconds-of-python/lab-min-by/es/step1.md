# Encuentra el valor mínimo de una lista basado en una función

Escribe una función llamada `min_by(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe mapear cada elemento de la lista a un valor utilizando la función proporcionada y luego devolver el valor mínimo.

```python
def min_by(lst, fn):
  return min(map(fn, lst))
```

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```
