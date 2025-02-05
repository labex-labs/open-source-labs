# Convert strings to datetime objects

The dates in the "datetime" column are currently strings. We want to convert these to datetime objects for easier manipulation.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```
