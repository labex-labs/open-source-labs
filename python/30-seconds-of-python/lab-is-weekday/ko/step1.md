# 날짜가 평일인지 확인하기

`is_weekday()`라는 Python 함수를 작성하여 날짜를 입력으로 받아 평일이면 `True`를, 주말이면 `False`를 반환합니다. 날짜가 제공되지 않으면 함수는 현재 날짜를 사용해야 합니다.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `datetime` 모듈을 가져옵니다.
2. `is_weekday()`라는 함수를 정의하고 날짜를 입력으로 받습니다. 날짜가 제공되지 않으면 현재 날짜를 사용합니다.
3. `datetime` 모듈의 `weekday()` 메서드를 사용하여 요일을 정수로 가져옵니다. `weekday()` 메서드는 0 (월요일) 에서 6 (일요일) 사이의 정수를 반환합니다.
4. 요일이 4 이하인지 확인합니다. 그렇다면 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.

```python
from datetime import datetime

def is_weekday(d = datetime.today()):
  return d.weekday() <= 4
```

```python
from datetime import date

is_weekday(date(2020, 10, 25)) # False
is_weekday(date(2020, 10, 28)) # True
```
