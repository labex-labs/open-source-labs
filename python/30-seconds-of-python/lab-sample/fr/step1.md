# Élément aléatoire dans une liste

Écrivez une fonction `random_element(lst)` qui prend une liste en argument et renvoie un élément aléatoire de cette liste.

- Utilisez `random.choice()` pour obtenir un élément aléatoire de `lst`.

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
