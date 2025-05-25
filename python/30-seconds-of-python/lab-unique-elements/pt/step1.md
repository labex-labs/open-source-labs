# Elementos Únicos em Lista

Escreva uma função Python chamada `unique_elements` que recebe uma lista como entrada e retorna uma nova lista contendo apenas os elementos únicos. Sua função deve realizar as seguintes etapas:

- Crie um `set` a partir da lista para descartar valores duplicados.
- Retorne uma `list` a partir do set.

Sua função deve ter a seguinte assinatura:

```python
def unique_elements(li: List) -> List:
```

```python
def unique_elements(li):
  return list(set(li))
```

```python
unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]
```
