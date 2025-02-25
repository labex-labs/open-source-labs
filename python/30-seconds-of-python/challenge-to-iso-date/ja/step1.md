# ISO 形式への日付変換

## 問題

`datetime.datetime` オブジェクトを引数として受け取り、ISO-8601 形式で表される日付を表す文字列を返す関数 `to_iso_date(d)` を作成します。この関数は、日付を ISO-8601 形式に変換するために `datetime.datetime.isoformat()` メソッドを使用する必要があります。

## 例

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # "2020-10-25T00:00:00"
```
