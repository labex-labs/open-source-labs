# Todos os Índices de um Valor

Escreva uma função Python chamada `index_of_all(lst, value)` que recebe uma lista `lst` e um valor `value` como argumentos e retorna uma lista de índices de todas as ocorrências de `value` em `lst`.

Para resolver este problema, você pode usar `enumerate()` e uma list comprehension para verificar cada elemento quanto à igualdade com `value` e adicionar `i` ao resultado.

```python
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]
```

```python
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
