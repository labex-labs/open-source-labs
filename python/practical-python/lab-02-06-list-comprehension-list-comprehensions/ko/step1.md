# 새로운 리스트 생성

리스트 컴프리헨션은 시퀀스의 각 요소에 연산을 적용하여 새로운 리스트를 생성합니다.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

또 다른 예시:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

일반적인 구문은 다음과 같습니다: `[ <expression> for <variable_name> in <sequence> ]`.
