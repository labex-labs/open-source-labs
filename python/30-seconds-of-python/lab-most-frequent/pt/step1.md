# Elemento Mais Frequente

Escreva uma função Python chamada `most_frequent(lst)` que recebe uma lista de inteiros como entrada e retorna o elemento mais frequente na lista. Se houver múltiplos elementos que aparecem o mesmo número de vezes e têm a maior frequência, retorne aquele que aparece primeiro na lista.

Para resolver este problema, você pode seguir estes passos:

1. Use `set()` para obter os valores únicos em `lst`.
2. Use `max()` para encontrar o elemento que tem o maior número de aparições.

Sua função deve ter a seguinte assinatura:

```python
def most_frequent(lst: List[int]) -> int:
```

```python
def most_frequent(lst):
  return max(set(lst), key = lst.count)
```

```python
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
```
