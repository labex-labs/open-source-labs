# ISO 日付を変換する

ISO-8601 形式で日付を表す文字列 `d` を受け取り、同じ日付と時刻を表す `datetime.datetime` オブジェクトを返す関数 `from_iso_date(d)` を作成します。

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
