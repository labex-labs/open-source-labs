# 字符串变位词

编写一个函数 `is_anagram(s1, s2)`，该函数接受两个字符串作为参数，如果它们是彼此的变位词，则返回 `True`，否则返回 `False`。该函数应不区分大小写，忽略空格、标点符号和特殊字符。

要解决此问题，你可以按以下步骤操作：

1. 使用 `str.isalnum()` 过滤掉非字母数字字符，并使用 `str.lower()` 将每个字符转换为小写。
2. 使用 `collections.Counter` 对每个字符串的结果字符进行计数，并比较结果。

```python
from collections import Counter

def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )
```

```python
is_anagram('#anagram', 'Nag a ram!')  # True
```
