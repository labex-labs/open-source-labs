# Encontrar el valor máximo de una lista basado en una función

Escribe una función `max_by(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe mapear cada elemento en `lst` a un valor usando la función `fn` proporcionada y luego devolver el valor máximo.

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
