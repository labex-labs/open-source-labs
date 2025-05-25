# 연습 문제 5.6: 간단한 Property

Property 는 객체에 "계산된 속성 (computed attributes)"을 추가하는 유용한 방법입니다. `stock.py`에서 `Stock` 객체를 생성했습니다. 객체에서 서로 다른 종류의 데이터를 추출하는 방식에 약간의 불일치가 있음을 확인하십시오.

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

특히, `cost`가 메서드이기 때문에 추가로 `()`를 추가해야 하는 방식을 확인하십시오.

`cost()`를 property 로 변환하면 `cost()`에 추가로 `()`를 제거할 수 있습니다. `Stock` 클래스를 가져와서 비용 계산이 다음과 같이 작동하도록 수정하십시오.

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost
49010.0
>>>
```

`s.cost()`를 함수로 호출해보고, `cost`가 property 로 정의되었으므로 작동하지 않는지 확인하십시오.

```python
>>> s.cost()
... fails ...
>>>
```

이 변경을 하면 이전의 `pcost.py` 프로그램이 중단될 수 있습니다. `cost()` 메서드에서 `()`를 제거해야 할 수도 있습니다.
