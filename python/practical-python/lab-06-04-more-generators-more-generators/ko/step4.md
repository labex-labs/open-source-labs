# 연습 문제 6.13: 제너레이터 표현식 (Generator Expressions)

제너레이터 표현식은 리스트 컴프리헨션 (list comprehension) 의 제너레이터 버전입니다. 예를 들어:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x109207e60>
>>> for n in squares:
...     print(n)
...
1
4
9
16
25
```

리스트 컴프리헨션과는 달리, 제너레이터 표현식은 한 번만 사용할 수 있습니다. 따라서 다른 for 루프를 시도하면 아무것도 얻을 수 없습니다:

```python
>>> for n in squares:
...     print(n)
...
>>>
```
