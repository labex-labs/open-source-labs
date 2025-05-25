# Timedelta Index 생성하기

시간 델타 (time delta) 를 사용하여 인덱스를 생성할 수 있습니다.

```python
# Generate a timedelta index
pd.TimedeltaIndex(["1 days", "1 days, 00:00:05", np.timedelta64(2, "D"), datetime.timedelta(days=2, seconds=2)])
```
