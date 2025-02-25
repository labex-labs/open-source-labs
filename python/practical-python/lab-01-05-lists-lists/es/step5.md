# Ordenamiento de listas

Las listas se pueden ordenar "in-place".

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Orden inverso
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# Funciona con cualquier dato ordenado
s = ['foo', 'bar','spam']
s.sort()                    # ['bar', 'foo','spam']
```

Utiliza `sorted()` si prefieres crear una nueva lista en lugar de modificar la original:

```python
t = sorted(s)               # s permanece inalterada, t contiene los valores ordenados
```
