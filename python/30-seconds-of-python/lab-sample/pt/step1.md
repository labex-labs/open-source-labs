# Elemento Aleatório em Lista

Escreva uma função `random_element(lst)` que recebe uma lista como argumento e retorna um elemento aleatório dessa lista.

- Use `random.choice()` para obter um elemento aleatório de `lst`.

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
