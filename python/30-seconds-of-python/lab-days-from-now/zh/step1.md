# 从现在起的天数

编写一个函数 `days_from_now(n)`，它接受一个整数 `n` 作为输入，并返回从今天起 `n` 天后的日期。

要解决这个问题，你可以按照以下步骤进行：

1. 导入 `datetime` 模块。
2. 使用 `date.today()` 方法获取当前日期。
3. 使用 `timedelta` 方法将 `n` 天添加到当前日期。
4. 返回新的日期。

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
