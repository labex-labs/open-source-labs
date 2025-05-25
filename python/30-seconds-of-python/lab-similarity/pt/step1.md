# Similaridade de Listas

Escreva uma função `similarity(a, b)` que recebe duas listas `a` e `b` como argumentos e retorna uma nova lista que contém apenas os elementos que existem em ambas `a` e `b`.

Para resolver este problema, podemos usar _list comprehension_ (compreensão de lista) para iterar sobre os elementos de `a` e verificar se eles existem em `b`. Se um elemento existir em ambas as listas, adicionamos ele a uma nova lista.

```python
def similarity(a, b):
  return [item for item in a if item in b]
```

```python
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```
