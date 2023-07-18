# Set epoch to the new default

To use modern dates at microsecond precision, we need to set the epoch to the new default, which is days since "1970-01-01T00:00:00".

```python
mdates.set_epoch('1970-01-01T00:00:00')
```
