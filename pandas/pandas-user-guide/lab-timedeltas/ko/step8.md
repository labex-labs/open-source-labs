# Timedelta Index 사용하기

Timedelta index 를 pandas 객체의 인덱스로 사용할 수 있습니다.

```python
# Use the timedelta index as the index of a pandas series
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```
