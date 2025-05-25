# 날짜 설정 및 임의 데이터 생성

시작 및 종료 날짜와 각 날짜 간의 차이를 나타내는 델타 (delta) 를 설정해야 합니다. 또한 예제를 위해 임의 데이터를 생성해야 합니다.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
