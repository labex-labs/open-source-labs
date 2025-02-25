# 今日からの日数

整数`n`を入力として受け取り、今日から`n`日後の日付を返す関数`days_from_now(n)`を書きましょう。

この問題を解くには、次の手順に従うことができます。

1. `datetime`モジュールをインポートします。
2. `date.today()`メソッドを使って現在の日付を取得します。
3. `timedelta`メソッドを使って現在の日付に`n`日を加えます。
4. 新しい日付を返します。

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
