# ISO 날짜 변환

ISO-8601 형식으로 날짜를 나타내는 문자열 `d`를 입력받아 동일한 날짜와 시간을 나타내는 `datetime.datetime` 객체를 반환하는 함수 `from_iso_date(d)`를 작성하십시오.

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
