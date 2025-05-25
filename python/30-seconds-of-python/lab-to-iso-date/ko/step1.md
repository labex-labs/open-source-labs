# 날짜를 ISO 형식으로 변환

`datetime.datetime` 객체를 인수로 받아 ISO-8601 형식으로 날짜를 나타내는 문자열을 반환하는 함수 `to_iso_date(d)`를 작성하십시오. 이 함수는 `datetime.datetime.isoformat()` 메서드를 사용하여 날짜를 ISO-8601 표현으로 변환해야 합니다.

```python
from datetime import datetime

def to_iso_date(d):
  return d.isoformat()
```

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # 2020-10-25T00:00:00
```
