# 날짜 차이 (일)

두 날짜 객체를 입력으로 받아 그 사이의 일수를 반환하는 함수 `days_diff(start, end)`를 작성하십시오. 이 함수는 `end`에서 `start`를 빼고 `datetime.timedelta.days`를 사용하여 일수 차이를 구해야 합니다.

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
