# Stock 클래스 다시 작성하기

이제 잘 정의된 `Structure` 기본 클래스가 있으므로 `Stock` 클래스를 다시 작성할 차례입니다. 이 기본 클래스를 사용하면 코드를 단순화하고 더 체계적으로 만들 수 있습니다. `Structure` 클래스는 `Stock` 클래스에서 재사용할 수 있는 일련의 공통 기능을 제공하며, 이는 코드 유지 관리 및 가독성에 큰 이점을 제공합니다.

## 새 Stock 클래스 만들기

`stock.py`라는 새 파일을 만들어 보겠습니다. 이 파일에는 다시 작성된 `Stock` 클래스가 포함됩니다. 다음은 `stock.py` 파일에 넣어야 하는 코드입니다.

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        주식 * 가격으로 비용을 계산합니다.
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        일정 수의 주식을 판매합니다.
        """
        self.shares -= nshares
```

이 새로운 `Stock` 클래스가 수행하는 작업을 자세히 살펴보겠습니다.

1.  `Structure` 클래스에서 상속합니다. 즉, `Stock` 클래스는 `Structure` 클래스에서 제공하는 모든 기능을 사용할 수 있습니다. 한 가지 이점은 `Structure` 클래스가 속성 할당을 자동으로 처리하므로 `__init__` 메서드를 직접 작성할 필요가 없다는 것입니다.
2.  `Stock` 클래스의 속성을 지정하는 튜플인 `_fields`를 정의합니다. 이러한 속성은 `name`, `shares` 및 `price`입니다.
3.  `cost` 속성은 주식의 총 비용을 계산하도록 정의됩니다. `shares` 수에 `price`를 곱합니다.
4.  `sell` 메서드는 주식 수를 줄이는 데 사용됩니다. 판매할 주식 수를 사용하여 이 메서드를 호출하면 현재 주식 수에서 해당 수를 뺍니다.

## 새 Stock 클래스 테스트하기

새 `Stock` 클래스가 예상대로 작동하는지 확인하기 위해 테스트 파일을 만들어야 합니다. 다음 코드로 `test_stock.py`라는 파일을 만들어 보겠습니다.

```python
# test_stock.py
from stock import Stock

# 주식 생성
s = Stock('GOOG', 100, 490.1)

# 속성 확인
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# 일부 주식 판매
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# 유효하지 않은 속성을 설정하려고 시도
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # 유효하지 않은 속성 ('price'여야 함)
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

이 테스트 파일에서는 먼저 `stock.py` 파일에서 `Stock` 클래스를 가져옵니다. 그런 다음 이름 'GOOG', 100 주, 가격 490.1 로 `Stock` 클래스의 인스턴스를 만듭니다. 주식의 속성을 인쇄하여 올바르게 설정되었는지 확인합니다. 그 후, 20 주를 판매하고 새로운 주식 수와 새로운 비용을 인쇄합니다. 마지막으로, 유효하지 않은 속성 `prices`를 설정하려고 합니다 (이것은 `price`여야 합니다). `Stock` 클래스가 올바르게 작동하면 `AttributeError`를 발생시켜야 합니다.

테스트를 실행하려면 터미널을 열고 다음 명령을 입력합니다.

```bash
python3 test_stock.py
```

예상 출력은 다음과 같습니다.

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## 단위 테스트 실행하기

이전 연습에서 단위 테스트가 있는 경우 새 구현에 대해 실행할 수 있습니다. 터미널에서 다음 명령을 입력합니다.

```bash
python3 teststock.py
```

일부 테스트가 실패할 수 있습니다. 이는 아직 구현하지 않은 특정 동작이나 메서드를 예상하기 때문일 수 있습니다. 걱정하지 마세요! 향후 연습에서 이 기반을 계속 구축할 것입니다.

## 진행 상황 검토

지금까지 달성한 내용을 잠시 검토해 보겠습니다.

1.  재사용 가능한 `Structure` 기본 클래스를 만들었습니다. 이 클래스는 다음과 같습니다.

    - 속성 할당을 자동으로 처리하여 많은 반복적인 코드를 작성하지 않아도 됩니다.
    - 객체를 인쇄하고 디버깅하기 쉽게 만드는 좋은 문자열 표현을 제공합니다.
    - 오류를 방지하기 위해 속성 이름을 제한하여 코드를 더욱 강력하게 만듭니다.

2.  `Stock` 클래스를 다시 작성했습니다. 다음은 다음과 같습니다.
    - 공통 기능을 재사용하기 위해 `Structure` 클래스에서 상속합니다.
    - 필드 및 도메인 관련 메서드만 정의하여 클래스를 집중적이고 깔끔하게 유지합니다.
    - 명확하고 단순한 설계를 통해 이해하고 유지 관리하기 쉽습니다.

이 접근 방식은 코드에 몇 가지 이점이 있습니다.

- 반복이 줄어들기 때문에 유지 관리가 더 용이합니다. 공통 기능에서 변경해야 하는 경우 `Structure` 클래스에서만 변경하면 됩니다.
- `Structure` 클래스에서 제공하는 더 나은 오류 검사로 인해 더 강력합니다.
- 각 클래스의 책임이 명확하기 때문에 가독성이 더 좋습니다.

향후 연습에서는 이 기반을 계속 구축하여 보다 정교한 주식 포트폴리오 관리 시스템을 만들 것입니다.
