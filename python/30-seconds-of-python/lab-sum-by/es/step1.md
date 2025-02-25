# Sumar una lista basada en una función

Escribe una función `sum_by(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe asignar a cada elemento de la lista un valor usando la función proporcionada y devolver la suma de los valores.

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
