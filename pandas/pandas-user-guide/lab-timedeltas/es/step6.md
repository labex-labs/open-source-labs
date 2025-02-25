# Convertir a una duración ISO 8601

Puedes convertir un timedelta en una cadena de duración ISO 8601.

```python
# Convert a timedelta to an ISO 8601 Duration string
pd.Timedelta(days=6, minutes=50, seconds=3, milliseconds=10, microseconds=10, nanoseconds=12).isoformat()
```
