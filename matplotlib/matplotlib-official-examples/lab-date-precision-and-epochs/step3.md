# Convert datetime to matplotlib date

Now that the epoch has been set, we can convert a `datetime` object to a Matplotlib date using the `mdates.date2num` function.

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
