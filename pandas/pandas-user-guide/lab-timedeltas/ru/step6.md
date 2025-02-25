# Преобразование в формат ISO 8601 длительности

Вы можете преобразовать временной интервал в строку формата ISO 8601 длительности.

```python
# Convert a timedelta to an ISO 8601 Duration string
pd.Timedelta(days=6, minutes=50, seconds=3, milliseconds=10, microseconds=10, nanoseconds=12).isoformat()
```
