# 오늘부터 며칠 후

정수 `n`을 입력으로 받아 오늘로부터 `n`일 후의 날짜를 반환하는 함수 `days_from_now(n)`을 작성하십시오.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `datetime` 모듈을 가져옵니다.
2. `date.today()` 메서드를 사용하여 현재 날짜를 가져옵니다.
3. `timedelta` 메서드를 사용하여 현재 날짜에 `n`일을 더합니다.
4. 새로운 날짜를 반환합니다.

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
