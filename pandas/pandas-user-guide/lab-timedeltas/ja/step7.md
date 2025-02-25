# 時間差分インデックスを作成する

時間差分を持つインデックスを生成することができます。

```python
# Generate a timedelta index
pd.TimedeltaIndex(["1 days", "1 days, 00:00:05", np.timedelta64(2, "D"), datetime.timedelta(days=2, seconds=2)])
```
