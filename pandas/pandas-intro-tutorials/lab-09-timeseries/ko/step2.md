# 문자열을 datetime 객체로 변환

"datetime" 열의 날짜는 현재 문자열입니다. 이러한 문자열을 더 쉽게 조작할 수 있도록 datetime 객체로 변환하려고 합니다.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```
