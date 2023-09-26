# Random Element in List

Write a function `random_element(lst)` that takes a list as an argument and returns a random element from that list.

- Use `random.choice()` to get a random element from `lst`.

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
