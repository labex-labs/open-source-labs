# Convert datetime to matplotlib date with new epoch

Now that the epoch has been set to the new default, we can convert a `datetime` object to a Matplotlib date using the `mdates.date2num` function.

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
