# 연습 문제 8.1: 유닛 테스트 작성 (Writing Unit Tests)

별도의 파일 `test_stock.py`에 `Stock` 클래스에 대한 일련의 유닛 테스트를 작성하십시오. 시작하기 위해 인스턴스 생성을 테스트하는 작은 코드 조각이 있습니다.

```python
# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

유닛 테스트를 실행하십시오. 다음과 같은 출력을 얻을 수 있습니다.

    .
    ----------------------------------------------------------------------
    Ran 1 tests in 0.000s

    OK

작동하는지 확인했으면 다음을 확인하는 추가 유닛 테스트를 작성하십시오.

- `s.cost` 속성이 올바른 값 (49010.0) 을 반환하는지 확인합니다.
- `s.sell()` 메서드가 올바르게 작동하는지 확인합니다. `s.shares`의 값을 적절하게 감소시켜야 합니다.
- `s.shares` 속성을 정수가 아닌 값으로 설정할 수 없는지 확인합니다.

마지막 부분의 경우 예외가 발생했는지 확인해야 합니다. 이를 수행하는 쉬운 방법은 다음과 같은 코드를 사용하는 것입니다.

```python
class TestStock(unittest.TestCase):
    ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
