# 리스트에서 무작위 요소

리스트를 인수로 받아 해당 리스트에서 무작위 요소를 반환하는 함수 `random_element(lst)`를 작성하십시오.

- `random.choice()`를 사용하여 `lst`에서 무작위 요소를 가져오십시오.

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
