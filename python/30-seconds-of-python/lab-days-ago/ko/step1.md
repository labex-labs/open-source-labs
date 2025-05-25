# 며칠 전

귀하의 과제는 정수 `n`을 인수로 받아 오늘로부터 `n`일 전의 날짜를 반환하는 `days_ago(n)` 함수를 작성하는 것입니다.

이 문제를 해결하려면 `datetime` 모듈의 `date` 클래스를 사용하여 현재 날짜를 가져오고, `timedelta` 클래스를 사용하여 현재 날짜에서 `n`일을 빼야 합니다.

```python
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```python
days_ago(5) # date(2020, 10, 23)
```
