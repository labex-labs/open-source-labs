# 转换 ISO 日期

## 问题

编写一个函数 `from_iso_date(d)`，它接受一个表示 ISO-8601 格式日期的字符串 `d`，并返回一个表示相同日期和时间的 `datetime.datetime` 对象。

## 示例

```python
from_iso_date('2020-10-28T12:30:59.000000') # 返回 datetime.datetime(2020, 10, 28, 12, 30, 59)
```
