# Diferença de Listas

Escreva uma função Python chamada `list_difference(a, b)` que recebe duas listas como argumentos e retorna a diferença entre elas. A função não deve filtrar valores duplicados. Para resolver este problema, você pode seguir estes passos:

1.  Crie um conjunto (set) a partir da segunda lista `b`.
2.  Use uma list comprehension na primeira lista `a` para manter apenas os valores que não estão contidos no conjunto `_b` criado anteriormente.
3.  Retorne a lista resultante.

```python
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]
```

```python
difference([1, 2, 3], [1, 2, 4]) # [3]
```
