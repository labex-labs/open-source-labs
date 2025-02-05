# 示例：一对多映射

问题：你想要将一个键映射到多个值。

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

与上一个示例类似，键 `IBM` 应该有两个不同的元组。

解决方案：使用 `defaultdict`。

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

`defaultdict` 确保每次你访问一个键时都会得到一个默认值。
