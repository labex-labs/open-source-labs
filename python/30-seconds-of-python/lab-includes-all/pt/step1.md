# Verificar se uma Lista Inclui Todos os Valores

Escreva uma função chamada `includes_all(lst, values)` que recebe duas listas como parâmetros. A função deve verificar se todos os valores na lista `values` estão incluídos na lista `lst`. Se todos os valores estiverem incluídos, a função deve retornar `True`. Se algum dos valores não estiver incluído, a função deve retornar `False`.

Para resolver este problema, você deve:

1.  Usar um loop `for` para iterar por cada valor na lista `values`.
2.  Verificar se o valor atual está incluído na lista `lst` usando o operador `in`.
3.  Se o valor não estiver incluído, retornar `False`.
4.  Se todos os valores estiverem incluídos, retornar `True`.

```python
def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
```

```python
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```
