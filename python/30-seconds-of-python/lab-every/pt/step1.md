# Testar se cada elemento da lista é truthy

Escreva uma função chamada `every(lst, fn = lambda x: x)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função deve retornar `True` se `fn` retornar `True` para cada elemento na lista, e `False` caso contrário. Se nenhuma função for fornecida, a função deve usar a função identidade (`lambda x: x`) por padrão.

Para resolver este problema, você precisará usar a função `all()` em combinação com `map()` e a função `fn` fornecida para verificar se `fn` retorna `True` para todos os elementos na lista.

```python
def every(lst, fn = lambda x: x):
  return all(map(fn, lst))
```

```python
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
```
