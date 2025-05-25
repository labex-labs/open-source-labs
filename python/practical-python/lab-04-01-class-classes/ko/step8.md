# 연습 문제 4.2: 메서드 추가하기 (Adding some Methods)

클래스를 사용하면 객체에 함수를 연결할 수 있습니다. 이것을 메서드라고 하며, 객체 내부에 저장된 데이터를 조작하는 함수입니다. `Stock` 객체에 `cost()` 및 `sell()` 메서드를 추가합니다. 다음과 같이 작동해야 합니다.

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s.cost()
49010.0
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>> s.cost()
36757.5
>>>
```
