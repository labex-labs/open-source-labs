# 날짜에 일수 더하기

두 개의 인수를 받는 함수 `add_days(n, d)`를 작성하십시오.

- `n`: 주어진 날짜에 더하거나 (양수) 빼야 (음수) 하는 일수를 나타내는 정수입니다.
- `d`: 일수를 더하거나 빼야 하는 날짜를 나타내는 선택적 인수입니다. 제공되지 않으면 현재 날짜가 사용되어야 합니다.

이 함수는 지정된 일수를 더하거나 뺀 후의 새 날짜를 나타내는 `datetime` 객체를 반환해야 합니다.

```python
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)
```

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```
