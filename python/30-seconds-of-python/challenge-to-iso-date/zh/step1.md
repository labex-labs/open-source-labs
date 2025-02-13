# 日期转 ISO 格式

## 问题

编写一个函数 `to_iso_date(d)`，它接受一个 `datetime.datetime` 对象作为参数，并返回一个以 ISO-8601 格式表示日期的字符串。该函数应使用 `datetime.datetime.isoformat()` 方法将日期转换为其 ISO-8601 表示形式。

## 示例

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # "2020-10-25T00:00:00"
```
