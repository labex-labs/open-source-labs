# Função para Verificar Duplicatas em uma Lista

Escreva uma função Python chamada `has_duplicates(lst)` que recebe uma lista como argumento e retorna `True` se a lista tiver algum elemento duplicado, caso contrário, retorna `False`.

Para resolver este problema, você pode seguir estes passos:

1.  Converta a lista em um conjunto (set) para remover duplicatas.
2.  Compare o comprimento do conjunto com o comprimento da lista original.
3.  Se os comprimentos forem iguais, então a lista não possui duplicatas, caso contrário, ela possui duplicatas.

```python
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
