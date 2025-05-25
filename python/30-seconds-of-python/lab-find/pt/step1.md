# Encontrar Valor Correspondente

Escreva uma função chamada `find(lst, fn)` que recebe uma lista `lst` e uma função de teste `fn` como argumentos. A função deve retornar o valor do primeiro elemento em `lst` para o qual `fn` retorna `True`. Se nenhum elemento satisfaz a função de teste, a função deve retornar `None`.

```python
def find(lst, fn):
  return next(x for x in lst if fn(x))
```

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
```
