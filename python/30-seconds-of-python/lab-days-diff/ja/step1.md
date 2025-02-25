# 日数の差

2 つの日付オブジェクトを入力として受け取り、それらの間の日数を返す関数 `days_diff(start, end)` を書きましょう。この関数は `end` から `start` を引き、日付の差を取得するために `datetime.timedelta.days` を使用する必要があります。

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
