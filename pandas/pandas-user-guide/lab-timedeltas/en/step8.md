# Use the Timedelta Index

You can use the timedelta index as the index of pandas objects.

```python
# Use the timedelta index as the index of a pandas series
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```
