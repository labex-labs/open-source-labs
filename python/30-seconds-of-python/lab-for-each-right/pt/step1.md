# Executar função para cada elemento da lista em ordem inversa

Escreva uma função `for_each_right(itr, fn)` que recebe uma lista `itr` e uma função `fn` como argumentos. A função deve executar `fn` uma vez para cada elemento em `itr`, começando pelo último.

```python
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```python
for_each_right([1, 2, 3], print) # 3 2 1
```
