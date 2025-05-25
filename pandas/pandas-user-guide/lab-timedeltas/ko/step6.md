# ISO 8601 Duration 으로 변환하기

Timedelta 를 ISO 8601 Duration 문자열로 변환할 수 있습니다.

```python
# Convert a timedelta to an ISO 8601 Duration string
pd.Timedelta(days=6, minutes=50, seconds=3, milliseconds=10, microseconds=10, nanoseconds=12).isoformat()
```
