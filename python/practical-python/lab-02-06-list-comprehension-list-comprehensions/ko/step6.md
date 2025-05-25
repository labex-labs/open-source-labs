# 연습 문제 2.19: 리스트 컴프리헨션 (List comprehensions)

구문에 익숙해지기 위해 몇 가지 간단한 리스트 컴프리헨션을 시도해 보세요.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

리스트 컴프리헨션이 데이터를 적절하게 변환하거나 필터링하여 새로운 리스트를 생성하는 방식을 확인하세요.
