# 日付範囲チャレンジ

## 問題

2 つの `datetime.date` オブジェクトを引数として受け取り、それらの間のすべての日付のリストを返す、`daterange(start, end)` という名前の Python 関数を書きましょう。このリストには開始日付が含まれるべきですが、終了日付は含まれません。

この問題を解くには、次の手順に従うことができます。

1. `datetime.timedelta.days` を使用して、`start` と `end` の間の日数を取得します。
2. `int()` を使用して結果を整数に変換し、`range()` を使用して各日を反復処理します。
3. リスト内包表記と `datetime.timedelta` を使用して、`datetime.date` オブジェクトのリストを作成します。

## 例

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
