# Diferença Simétrica (Symmetric Difference)

Escreva uma função `symmetric_difference(a, b)` que recebe duas listas como argumentos e retorna a sua diferença simétrica como uma lista. A função não deve filtrar valores duplicados.

Para resolver este problema, você pode seguir estes passos:

1.  Crie um conjunto (set) a partir de cada lista.
2.  Use uma compreensão de lista (list comprehension) em cada uma delas para manter apenas os valores que não estão contidos no conjunto criado anteriormente da outra.
3.  Concatene as duas listas obtidas no passo 2.

```python
def symmetric_difference(a, b):
  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

```python
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
