# 列表中的随机元素

编写一个函数 `random_element(lst)`，它接受一个列表作为参数，并从该列表中返回一个随机元素。

- 使用 `random.choice()` 从 `lst` 中获取一个随机元素。

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
