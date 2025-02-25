# 時間差分インデックスを使用する

時間差分インデックスを pandas オブジェクトのインデックスとして使用することができます。

```python
# Use the timedelta index as the index of a pandas series
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```
