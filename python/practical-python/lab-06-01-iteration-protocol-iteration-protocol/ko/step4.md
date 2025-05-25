# 연습 문제 6.1: 반복 시연 (Iteration Illustrated)

다음 리스트를 생성합니다.

```python
a = [1,9,4,25,16]
```

이 리스트를 수동으로 반복합니다. `__iter__()`를 호출하여 이터레이터 (iterator) 를 얻고, `__next__()` 메서드를 호출하여 연속적인 요소를 얻습니다.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

`next()` 내장 함수는 이터레이터의 `__next__()` 메서드를 호출하는 단축키입니다. 파일을 대상으로 사용해 보세요.

```python
>>> f = open('portfolio.csv')
>>> f.__iter__()    # 참고: 이것은 파일 자체를 반환합니다 (Note: This returns the file itself)
<_io.TextIOWrapper name='portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

파일의 끝에 도달할 때까지 `next(f)`를 계속 호출합니다. 어떤 일이 일어나는지 확인하세요.
