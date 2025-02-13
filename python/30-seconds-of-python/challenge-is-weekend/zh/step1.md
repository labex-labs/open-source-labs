# 判断日期是否为周末

## 问题

编写一个函数 `is_weekend(d)`，该函数接受一个日期对象作为输入，如果给定日期是周末，则返回 `True`，否则返回 `False`。如果未提供参数，该函数应使用当前日期。

要解决此问题，你可以按以下步骤操作：

1. 使用 `datetime.datetime.weekday()` 方法获取星期几的整数值。
2. 检查星期几是否大于 `4`。如果是，则返回 `True`，否则返回 `False`。

## 示例

```python
from datetime import date

assert is_weekend(date(2022, 1, 1)) == True
assert is_weekend(date(2022, 1, 3)) == False
assert is_weekend() == False # 当前日期不是周末
```
