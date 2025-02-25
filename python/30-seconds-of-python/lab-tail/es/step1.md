# Cola de lista

Escribe una función `tail(lst)` que tome una lista como argumento y devuelva todos los elementos de la lista excepto el primero. Si la lista contiene solo un elemento, devuelve toda la lista.

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
