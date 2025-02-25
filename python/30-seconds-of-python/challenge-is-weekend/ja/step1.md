# 日付が土日かどうか

## 問題

日付オブジェクトを入力として受け取り、与えられた日付が土日の場合は `True` を返し、そうでない場合は `False` を返す関数 `is_weekend(d)` を書きます。引数が提供されない場合、関数は現在の日付を使用する必要があります。

この問題を解決するには、次の手順を辿ることができます。

1. `datetime.datetime.weekday()` メソッドを使用して、曜日を整数として取得します。
2. 曜日が `4` より大きいかどうかを確認します。そうであれば `True` を返し、そうでなければ `False` を返します。

## 例

```python
from datetime import date

assert is_weekend(date(2022, 1, 1)) == True
assert is_weekend(date(2022, 1, 3)) == False
assert is_weekend() == False # current date is not a weekend
```
