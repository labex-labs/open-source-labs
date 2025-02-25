# Elemento aleatorio en una lista

Escribe una función `random_element(lst)` que tome una lista como argumento y devuelva un elemento aleatorio de esa lista.

- Utiliza `random.choice()` para obtener un elemento aleatorio de `lst`.

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
