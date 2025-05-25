# Print 로 디버깅하기

`print()` 디버깅은 매우 흔하게 사용됩니다.

_팁: `repr()`을 사용하세요._

```python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()`은 값의 정확한 표현을 보여줍니다. _예쁘게_ 출력되는 것은 아닙니다.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# NO `repr`
>>> print(x)
3.4
# WITH `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
