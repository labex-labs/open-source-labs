# 演算を行う

時間差分に対して数学的演算を行うことができます。

```python
# Subtract two timedeltas
s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
s - s.max()
```
