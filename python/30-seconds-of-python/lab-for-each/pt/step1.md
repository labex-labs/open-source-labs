# Executar Função para Cada Elemento da Lista

Escreva uma função `for_each(itr, fn)` que recebe uma lista `itr` e uma função `fn` como argumentos. A função deve executar `fn` uma vez para cada elemento em `itr`.

```python
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```python
for_each([1, 2, 3], print) # 1 2 3
```
