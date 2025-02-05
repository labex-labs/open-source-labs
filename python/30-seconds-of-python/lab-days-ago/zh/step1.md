# 若干天前

你的任务是编写一个名为 `days_ago(n)` 的函数，它接受一个整数 `n` 作为参数，并返回从今天起 `n` 天前的日期。

要解决这个问题，你需要使用 `datetime` 模块中的 `date` 类来获取当前日期，并使用 `timedelta` 类从当前日期中减去 `n` 天。

```python
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```python
days_ago(5) # date(2020, 10, 23)
```
