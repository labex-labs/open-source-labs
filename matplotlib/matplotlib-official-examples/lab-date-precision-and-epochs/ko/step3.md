# datetime 을 matplotlib 날짜로 변환

이제 에포크가 설정되었으므로 `datetime` 객체를 `mdates.date2num` 함수를 사용하여 Matplotlib 날짜로 변환할 수 있습니다.

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
