# 날짜 범위 (Date Range)

`daterange(start, end)`라는 Python 함수를 작성하세요. 이 함수는 두 개의 `datetime.date` 객체를 인수로 받아 그 사이의 모든 날짜 목록을 반환합니다. 목록에는 시작 날짜는 포함되지만 종료 날짜는 포함되지 않아야 합니다.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `datetime.timedelta.days`를 사용하여 `start`와 `end` 사이의 일수를 구합니다.
2. `int()`를 사용하여 결과를 정수로 변환하고 `range()`를 사용하여 각 날짜를 반복합니다.
3. 리스트 컴프리헨션 (list comprehension) 과 `datetime.timedelta`를 사용하여 `datetime.date` 객체의 목록을 생성합니다.

```python
from datetime import timedelta, date

def daterange(start, end):
  return [start + timedelta(n) for n in range(int((end - start).days))]
```

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
