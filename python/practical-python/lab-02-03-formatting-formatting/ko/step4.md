# format() 메서드

인수 또는 키워드 인수에 서식을 적용할 수 있는 `format()` 메서드가 있습니다.

```python
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)
'       IBM        100      91.10'
>>> '{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91.10'
>>>
```

솔직히 말해서, `format()`은 약간 장황합니다. 저는 f-string 을 선호합니다.
