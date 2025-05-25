# 연산 수행하기

Timedelta 에 대해 수학적 연산을 수행할 수 있습니다.

```python
# Subtract two timedeltas
s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
s - s.max()
```
