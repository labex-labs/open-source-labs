# 날짜가 주말인지 확인

날짜 객체를 입력으로 받아 주어진 날짜가 주말이면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `is_weekend(d)`를 작성하십시오. 인수가 제공되지 않으면 함수는 현재 날짜를 사용해야 합니다.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `datetime.datetime.weekday()` 메서드를 사용하여 요일을 정수로 가져옵니다.
2. 요일이 `4`보다 큰지 확인합니다. 그렇다면 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.

```python
from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
```

```python
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```
