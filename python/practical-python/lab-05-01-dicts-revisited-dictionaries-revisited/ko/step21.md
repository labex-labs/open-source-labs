# 연습 문제 5.4: 바운드 메서드 (Bound methods)

Python 의 미묘한 특징은 메서드를 호출하는 것이 실제로 두 단계와 바운드 메서드라고 하는 것을 포함한다는 것입니다. 예를 들어:

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

바운드 메서드는 실제로 메서드를 호출하는 데 필요한 모든 조각을 포함합니다. 예를 들어, 메서드를 구현하는 함수의 기록을 유지합니다.

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

이것은 `Stock` 딕셔너리에서 찾은 것과 동일한 값입니다.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

바운드 메서드는 또한 `self` 인수인 인스턴스를 기록합니다.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

`()`를 사용하여 함수를 호출하면 모든 조각이 함께 결합됩니다. 예를 들어, `s(25)`를 호출하면 실제로 다음과 같은 일이 발생합니다.

```python
>>> s.__func__(s.__self__, 25)    # Same as s(25)
>>> goog.shares
50
>>>
```
