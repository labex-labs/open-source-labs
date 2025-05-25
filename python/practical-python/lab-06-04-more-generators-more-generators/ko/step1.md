# 제너레이터 표현식 (Generator Expressions)

리스트 컴프리헨션 (list comprehension) 의 제너레이터 버전입니다.

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

리스트 컴프리헨션과의 차이점:

- 리스트를 구성하지 않습니다.
- 유일한 용도는 반복 (iteration) 입니다.
- 한 번 사용하면 재사용할 수 없습니다.

일반적인 구문:

```python
(<expression> for i in s if <conditional>)
```

함수 인수로도 사용할 수 있습니다.

```python
sum(x*x for x in a)
```

모든 이터러블 (iterable) 에 적용할 수 있습니다.

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

제너레이터 표현식의 주요 사용 사례는 시퀀스에 대해 어떤 계산을 수행하지만 결과를 한 번만 사용하는 코드입니다. 예를 들어, 파일에서 모든 주석을 제거하는 경우입니다.

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
    ...
f.close()
```

제너레이터를 사용하면 코드가 더 빠르게 실행되고 메모리를 적게 사용합니다. 스트림에 적용되는 필터와 같습니다.
