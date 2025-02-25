# 日付が土日かどうか

日付オブジェクトを入力として受け取り、与えられた日付が土日の場合は `True` を返し、それ以外の場合は `False` を返す `is_weekend(d)` 関数を作成します。引数が提供されない場合、関数は現在の日付を使用する必要があります。

この問題を解決するには、次の手順を辿ることができます。

1. `datetime.datetime.weekday()` メソッドを使用して、曜日を整数として取得します。
2. 曜日が `4` より大きいかどうかを確認します。そうであれば `True` を返し、そうでなければ `False` を返します。

```python
from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
```

```python
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```
