# API 挑战：类型提示

函数可以为参数和返回值附加可选的类型提示。例如：

```python
def add(x:int, y:int) -> int:
    return x + y
```

`typing` 模块有其他类用于表示更复杂的类型，包括容器类型。例如：

```python
from typing import List

def sum_squares(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n*n
    return total
```

你的挑战：修改`reader.py`中的代码，使所有函数都有类型提示。尽量使类型提示尽可能准确。为此，你可能需要查阅 [typing 模块](https://docs.python.org/3/library/typing.html) 的文档。
