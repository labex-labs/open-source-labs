# Encontrar o Último Valor Correspondente

Escreva uma função `find_last(lst, fn)` que recebe uma lista `lst` e uma função de teste `fn` como argumentos. A função deve retornar o valor do último elemento em `lst` para o qual `fn` retorna `True`. Se nenhum elemento satisfaz a função de teste, a função deve retornar `None`.

Para resolver este problema, você deve usar uma list comprehension (compreensão de lista) e `next()` para iterar pela lista em ordem inversa e retornar o último elemento que satisfaz a função de teste.

```python
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```
