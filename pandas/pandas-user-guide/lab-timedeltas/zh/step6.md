# 转换为 ISO 8601 持续时间格式

你可以将一个时间增量转换为 ISO 8601 持续时间字符串。

```python
# 将一个时间增量转换为 ISO 8601 持续时间字符串
pd.Timedelta(days=6, minutes=50, seconds=3, milliseconds=10, microseconds=10, nanoseconds=12).isoformat()
```
