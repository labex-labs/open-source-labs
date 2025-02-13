# 检查日期是否为工作日

## 问题

编写一个名为 `is_weekday()` 的 Python 函数，该函数接受一个日期作为输入，如果是工作日则返回 `True`，如果是周末则返回 `False`。如果未提供日期，该函数应使用当前日期。

要解决此问题，你可以按照以下步骤操作：

1. 导入 `datetime` 模块。
2. 定义一个名为 `is_weekday()` 的函数，该函数接受一个日期作为输入。如果未提供日期，则使用当前日期。
3. 使用 `datetime` 模块的 `weekday()` 方法获取星期几作为整数。`weekday()` 方法返回一个介于 0（星期一）和 6（星期日）之间的整数。
4. 检查星期几是否小于或等于 4。如果是，则返回 `True`，否则返回 `False`。

## 示例

以下是你的函数应有的行为示例：

```python
from datetime import date

assert is_weekday(date(2022, 11, 11)) == False
assert is_weekday(date(2022, 11, 14)) == True
assert is_weekday(date(2022, 11, 12)) == False
assert is_weekday(date(2022, 11, 13)) == False
```
