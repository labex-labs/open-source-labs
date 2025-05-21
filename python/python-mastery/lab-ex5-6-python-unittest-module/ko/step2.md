# 테스트 케이스 확장하기

이제 기본적인 테스트 케이스를 만들었으므로 테스트 범위를 확장할 차례입니다. 더 많은 테스트를 추가하면 `Stock` 클래스의 나머지 기능을 다루는 데 도움이 됩니다. 이렇게 하면 클래스의 모든 측면이 예상대로 작동하는지 확인할 수 있습니다. `TestStock` 클래스를 수정하여 여러 메서드와 속성에 대한 테스트를 포함시킬 것입니다.

1. `teststock.py` 파일을 엽니다. `TestStock` 클래스 내부에 몇 가지 새로운 테스트 메서드를 추가할 것입니다. 이러한 메서드는 `Stock` 클래스의 다른 부분을 테스트합니다. 다음은 추가해야 하는 코드입니다.

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

각 테스트가 수행하는 작업을 자세히 살펴보겠습니다.

- `test_create_keyword_args`: 이 테스트는 키워드 인수를 사용하여 `Stock` 객체를 생성할 수 있는지 확인합니다. 객체의 속성이 올바르게 설정되었는지 확인합니다.
- `test_cost`: 이 테스트는 `Stock` 객체의 `cost` 속성이 올바른 값 (주식 수에 가격을 곱한 값) 을 반환하는지 확인합니다.
- `test_sell`: 이 테스트는 `Stock` 객체의 `sell()` 메서드가 일부 주식을 판매한 후 주식 수를 올바르게 업데이트하는지 확인합니다.
- `test_from_row`: 이 테스트는 `from_row()` 클래스 메서드가 데이터 행에서 새 `Stock` 인스턴스를 생성할 수 있는지 확인합니다.
- `test_repr`: 이 테스트는 `Stock` 객체의 `__repr__()` 메서드가 예상 문자열 표현을 반환하는지 확인합니다.
- `test_eq`: 이 테스트는 `__eq__()` 메서드가 두 `Stock` 객체를 올바르게 비교하여 동일한지 확인하는지 확인합니다.

2. 이러한 테스트 메서드를 추가한 후 `teststock.py` 파일을 저장합니다. 그런 다음 터미널에서 다음 명령을 사용하여 테스트를 다시 실행합니다.

```bash
python3 teststock.py
```

모든 테스트가 통과하면 다음과 같은 출력이 표시됩니다.

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

출력의 7 개의 점은 각 테스트를 나타냅니다. 각 점은 테스트가 성공적으로 통과했음을 나타냅니다. 따라서 7 개의 점이 보이면 7 개의 테스트가 모두 통과했음을 의미합니다.
