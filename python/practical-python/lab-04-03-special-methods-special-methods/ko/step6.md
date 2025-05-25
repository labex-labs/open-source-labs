# 바운드 메서드 (Bound Methods)

함수 호출 연산자 `()`에 의해 아직 호출되지 않은 메서드는 *바운드 메서드*로 알려져 있습니다. 이는 메서드가 생성된 인스턴스에서 작동합니다.

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

바운드 메서드는 종종 부주의한 명확하지 않은 오류의 원인이 됩니다. 예를 들어:

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

또는 디버깅하기 어려운 교활한 동작이 발생할 수 있습니다.

```python
f = open(filename, 'w')
...
f.close     # Oops, Didn't do anything at all. `f` still open.
```

이 두 경우 모두, 오류는 후행 괄호를 포함하는 것을 잊어버려서 발생합니다. 예를 들어, `s.cost()` 또는 `f.close()`와 같습니다.
