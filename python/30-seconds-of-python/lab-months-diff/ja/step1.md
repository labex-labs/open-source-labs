# 日付の差

2 つの日付オブジェクトを引数に取り、それらの間の月の差を返す `months_diff(start, end)` という関数を作成してください。この関数は以下のことを行う必要があります。

1. `end` から `start` を引き、`datetime.timedelta.days` を使用して日数の差を取得します。
2. 30 で割り、`math.ceil()` を使用して月の差を取得します（切り上げ）。

```python
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
