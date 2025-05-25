# Verificar se algum valor em uma lista está incluído em outra lista

Escreva uma função `includes_any(lst, values)` que recebe duas listas como argumentos. A função deve verificar se algum elemento em `values` está incluído em `lst`. Se qualquer valor for encontrado, a função deve retornar `True`; caso contrário, deve retornar `False`.

Para resolver este problema, você pode usar um loop `for` para iterar por cada valor em `values`. Em seguida, você pode usar o operador `in` para verificar se o valor está incluído em `lst`. Se um valor for encontrado, retorne `True`. Se nenhum valor for encontrado, retorne `False`.

```python
def includes_any(lst, values):
  for v in values:
    if v in lst:
      return True
  return False
```

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
