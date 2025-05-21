# 예외 테스트하기

테스트는 소프트웨어 개발의 중요한 부분이며, 그 중요한 측면 중 하나는 코드가 오류 조건을 적절하게 처리할 수 있도록 하는 것입니다. Python 에서 `unittest` 모듈은 특정 예외가 예상대로 발생했는지 테스트하는 편리한 방법을 제공합니다.

1. `teststock.py` 파일을 엽니다. 예외를 확인하도록 설계된 몇 가지 테스트 메서드를 추가할 것입니다. 이러한 테스트는 잘못된 입력을 만났을 때 코드가 올바르게 동작하는지 확인하는 데 도움이 됩니다.

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

이제 이러한 예외 테스트가 어떻게 작동하는지 이해해 보겠습니다.

- `with self.assertRaises(ExceptionType):` 문은 컨텍스트 관리자 (context manager) 를 생성합니다. 이 컨텍스트 관리자는 `with` 블록 내부의 코드가 지정된 예외를 발생시키는지 확인합니다.
- 예상된 예외가 `with` 블록 내에서 발생하면 테스트가 통과합니다. 이는 코드가 잘못된 입력을 올바르게 감지하고 적절한 오류를 발생시키고 있음을 의미합니다.
- 예외가 발생하지 않거나 다른 예외가 발생하면 테스트가 실패합니다. 이는 코드가 예상대로 잘못된 입력을 처리하지 못할 수 있음을 나타냅니다.

이러한 테스트는 다음 시나리오를 확인하도록 설계되었습니다.

- `shares` 속성을 문자열로 설정하면 `TypeError`가 발생해야 합니다. `shares`는 숫자여야 하기 때문입니다.
- `shares` 속성을 음수로 설정하면 `ValueError`가 발생해야 합니다. 주식 수는 음수가 될 수 없기 때문입니다.
- `price` 속성을 문자열로 설정하면 `TypeError`가 발생해야 합니다. `price`는 숫자여야 하기 때문입니다.
- `price` 속성을 음수로 설정하면 `ValueError`가 발생해야 합니다. 가격은 음수가 될 수 없기 때문입니다.
- 존재하지 않는 속성 `share`(누락된 's'에 유의) 를 설정하려고 하면 `AttributeError`가 발생해야 합니다. 올바른 속성 이름은 `shares`이기 때문입니다.

2. 이러한 테스트 메서드를 추가한 후 `teststock.py` 파일을 저장합니다. 그런 다음 터미널에서 다음 명령을 사용하여 모든 테스트를 실행합니다.

```bash
python3 teststock.py
```

모든 것이 올바르게 작동하면 12 개의 모든 테스트가 통과했음을 나타내는 출력이 표시됩니다. 출력은 다음과 같습니다.

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

12 개의 점은 지금까지 작성한 모든 테스트를 나타냅니다. 이전 단계에서 7 개의 테스트가 있었고, 방금 5 개를 더 추가했습니다. 이 출력은 코드가 예상대로 예외를 처리하고 있음을 보여주며, 이는 잘 테스트된 프로그램의 훌륭한 징후입니다.
