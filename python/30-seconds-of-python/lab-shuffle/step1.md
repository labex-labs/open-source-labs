# Shuffle List

Write a function `shuffle(lst)` that takes a list as input and returns a new list with the same items in a randomized order. Your function should use the Fisher-Yates algorithm to shuffle the items in the list.

The Fisher-Yates algorithm works as follows:

1. Start with the last item in the list.
2. Generate a random index between 0 and the current index.
3. Swap the item at the current index with the item at the random index.
4. Move to the next item in the list and repeat steps 2-3 until all items have been shuffled.

Your function should not modify the original list. Instead, it should create a new list with the shuffled items.

You can assume that the input list will contain at least one item.

```py
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```py
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
