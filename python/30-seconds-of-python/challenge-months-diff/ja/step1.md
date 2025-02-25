# 日付差のチャレンジ

## 問題

`months_diff(start, end)`という関数を書きなさい。この関数は2つの日付オブジェクトを受け取り、それらの月差を返します。この関数は以下のことを行う必要があります。

1. `end`から`start`を引き、`datetime.timedelta.days`を使って日付の差を取得します。
2. 30で割り、`math.ceil()`を使って月差を取得します（切り上げ）。

## 例

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
