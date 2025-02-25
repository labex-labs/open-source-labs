# ISO 日付を変換する

## 問題

ISO-8601 形式で日付を表す文字列 `d` を受け取り、同じ日付と時刻を表す `datetime.datetime` オブジェクトを返す関数 `from_iso_date(d)` を書きなさい。

## 例

```python
from_iso_date('2020-10-28T12:30:59.000000') # datetime.datetime(2020, 10, 28, 12, 30, 59) を返す
```
