# 메서드 호출

메서드 호출은 두 단계의 프로세스입니다.

1.  Lookup: `.` 연산자
2.  Method call: `()` 연산자

```python
>>> s = stock.Stock('GOOG',100,490.10)
>>> c = s.cost  # Lookup
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()         # Method call
49010.0
>>>
```
