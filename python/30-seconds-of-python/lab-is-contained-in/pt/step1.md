# Contenção de Lista (List Containment)

Escreva uma função `is_contained_in(a, b)` que recebe duas listas como argumentos e retorna `True` se todos os elementos da lista `a` estão contidos na lista `b`, independentemente da ordem. Caso contrário, a função deve retornar `False`.

Para resolver este problema, você pode usar a seguinte abordagem:

1.  Iterar por cada valor único na lista `a`.
2.  Para cada valor, verificar se ele aparece mais vezes na lista `a` do que na lista `b`.
3.  Se algum valor aparecer mais vezes na lista `a` do que na lista `b`, retornar `False`.
4.  Se todos os valores na lista `a` aparecerem na lista `b` pelo menos tantas vezes quanto aparecem na lista `a`, retornar `True`.

```python
def is_contained_in(a, b):
  for v in set(a):
    if a.count(v) > b.count(v):
      return False
  return True
```

```python
is_contained_in([1, 4], [2, 4, 1]) # True
```
