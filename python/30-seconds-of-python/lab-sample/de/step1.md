# Zufälliges Element in Liste

Schreibe eine Funktion `random_element(lst)`, die eine Liste als Argument nimmt und ein zufälliges Element aus dieser Liste zurückgibt.

- Verwende `random.choice()`, um ein zufälliges Element aus `lst` zu erhalten.

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
