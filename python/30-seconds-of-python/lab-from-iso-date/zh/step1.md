# 转换 ISO 日期

编写一个函数 `from_iso_date(d)`，它接受一个表示 ISO-8601 格式日期的字符串 `d`，并返回一个表示相同日期和时间的 `datetime.datetime` 对象。

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
