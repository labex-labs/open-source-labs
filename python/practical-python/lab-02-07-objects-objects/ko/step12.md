# 연습 문제 2.25: 딕셔너리 만들기 (Making dictionaries)

`dict()` 함수가 키 이름과 값의 시퀀스가 있는 경우 딕셔너리를 쉽게 만들 수 있다는 것을 기억하십니까? 열 헤더에서 딕셔너리를 만들어 봅시다.

```python
>>> headers
['name', 'shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```

물론, 리스트 컴프리헨션 (list-comprehension) 실력이 있다면, 딕셔너리 컴프리헨션 (dict-comprehension) 을 사용하여 전체 변환을 한 단계로 수행할 수 있습니다.

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```
