# In eine ISO 8601-Dauer umwandeln

Sie können ein Zeitintervall (Timedelta) in einen ISO 8601-Dauerstring umwandeln.

```python
# Convert a timedelta to an ISO 8601 Duration string
pd.Timedelta(days=6, minutes=50, seconds=3, milliseconds=10, microseconds=10, nanoseconds=12).isoformat()
```
