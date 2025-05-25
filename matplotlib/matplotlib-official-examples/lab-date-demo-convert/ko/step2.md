# 날짜 및 델타 정의

다음으로, datetime 라이브러리를 사용하여 날짜와 델타 값을 정의합니다. 날짜 범위는 2000 년 3 월 2 일부터 2000 년 3 월 6 일까지이며, 6 시간 간격으로 설정됩니다. 다음 코드를 복사하여 붙여넣으십시오:

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
