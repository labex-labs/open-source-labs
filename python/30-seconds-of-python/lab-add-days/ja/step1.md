# 日付に日数を加える

`add_days(n, d)` という関数を作成します。この関数には2つの引数が渡されます。

- `n`：指定された日付から加算する日数（正の場合）または減算する日数（負の場合）を表す整数。
- `d`：日数を加算または減算する対象の日付を表すオプションの引数。指定されない場合、現在の日付が使用されます。

この関数は、指定された日数を加算または減算した後の新しい日付を表す `datetime` オブジェクトを返す必要があります。

```python
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)
```

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```
