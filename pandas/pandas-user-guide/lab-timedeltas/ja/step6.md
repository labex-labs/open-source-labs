# ISO 8601 期間形式に変換する

時間差分を ISO 8601 期間形式の文字列に変換することができます。

```python
# Convert a timedelta to an ISO 8601 Duration string
pd.Timedelta(days=6, minutes=50, seconds=3, milliseconds=10, microseconds=10, nanoseconds=12).isoformat()
```
