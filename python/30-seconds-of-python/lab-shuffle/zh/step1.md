# 打乱列表

编写一个函数 `shuffle(lst)`，它接受一个列表作为输入，并返回一个新列表，其中包含相同的元素，但顺序是随机的。你的函数应该使用 Fisher-Yates 算法来打乱列表中的元素。

Fisher-Yates 算法的工作原理如下：

1. 从列表的最后一个元素开始。
2. 在 0 到当前索引之间生成一个随机索引。
3. 将当前索引处的元素与随机索引处的元素交换。
4. 移动到列表中的下一个元素，并重复步骤 2 - 3，直到所有元素都被打乱。

你的函数不应修改原始列表。相反，它应该创建一个包含打乱后元素的新列表。

你可以假设输入列表将至少包含一个元素。

```python
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

```python
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
