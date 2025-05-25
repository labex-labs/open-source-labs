# Encontrar Todos os Índices Correspondentes

Escreva uma função `find_index_of_all(lst, fn)` que recebe uma lista `lst` e uma função de teste `fn` como argumentos e retorna uma lista de índices de todos os elementos em `lst` para os quais `fn` retorna `True`.

### Entrada

- Uma lista `lst` de inteiros.
- Uma função de teste `fn` que recebe um inteiro como entrada e retorna um valor booleano.

### Saída

- Uma lista de inteiros representando os índices de todos os elementos em `lst` para os quais `fn` retorna `True`.

```python
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
