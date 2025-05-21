# 클래스 변수와 상속

이 단계에서는 클래스 변수가 상속과 어떻게 상호 작용하는지, 그리고 사용자 정의 메커니즘으로 어떻게 사용될 수 있는지 살펴보겠습니다. Python 에서 상속을 사용하면 하위 클래스가 기본 클래스에서 속성과 메서드를 상속받을 수 있습니다. 클래스 변수는 클래스의 특정 인스턴스가 아닌 클래스 자체에 속하는 변수입니다. 이러한 것들이 함께 작동하는 방식을 이해하는 것은 유연하고 유지 관리 가능한 코드를 만드는 데 매우 중요합니다.

## 상속에서의 클래스 변수

하위 클래스가 기본 클래스에서 상속될 때, 기본 클래스의 클래스 변수에 자동으로 액세스할 수 있습니다. 그러나 하위 클래스는 이러한 클래스 변수를 재정의할 수 있습니다. 그렇게 함으로써 하위 클래스는 기본 클래스에 영향을 주지 않고 동작을 변경할 수 있습니다. 이는 특정 요구 사항에 따라 하위 클래스의 동작을 사용자 정의할 수 있으므로 매우 강력한 기능입니다.

## 특수화된 Stock 클래스 만들기

`Stock` 클래스의 하위 클래스를 만들어 보겠습니다. 이를 `DStock`이라고 부르겠습니다. 여기서 D 는 Decimal Stock 을 의미합니다. `DStock`과 일반 `Stock` 클래스의 주요 차이점은 `DStock`이 `float` 대신 가격 값에 `Decimal` 유형을 사용한다는 것입니다. 금융 계산에서 정밀도는 매우 중요하며, `Decimal` 유형은 `float`에 비해 더 정확한 십진수 산술 연산을 제공합니다.

이 하위 클래스를 만들려면 `decimal_stock.py`라는 새 파일을 만듭니다. 이 파일에 넣어야 할 코드는 다음과 같습니다.

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    A specialized version of Stock that uses Decimal for prices
    """
    types = (str, int, Decimal)  # Override the types class variable

# Test the subclass
if __name__ == "__main__":
    # Create a DStock from row data
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # For comparison, create a regular Stock from the same data
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

위 코드로 `decimal_stock.py` 파일을 만든 후에는 결과를 확인하기 위해 실행해야 합니다. 터미널을 열고 다음 단계를 따르세요.

```bash
cd ~/project
python decimal_stock.py
```

다음과 유사한 출력이 표시되어야 합니다.

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## 클래스 변수와 상속에 대한 주요 사항

이 예제에서 몇 가지 중요한 결론을 도출할 수 있습니다.

1. `DStock` 클래스는 `cost()` 메서드와 같은 `Stock` 클래스의 모든 메서드를 다시 정의하지 않고 상속받습니다. 이는 상속의 주요 장점 중 하나이며, 중복된 코드를 작성하지 않아도 됩니다.
2. `types` 클래스 변수를 간단히 재정의함으로써 `DStock`의 새 인스턴스를 생성할 때 데이터가 변환되는 방식을 변경했습니다. 이는 클래스 변수를 사용하여 하위 클래스의 동작을 사용자 정의하는 방법을 보여줍니다.
3. 기본 클래스인 `Stock`은 변경되지 않고 여전히 `float` 값을 사용합니다. 즉, 하위 클래스에 대한 변경 사항이 기본 클래스에 영향을 미치지 않으며, 이는 좋은 설계 원칙입니다.
4. `from_row()` 클래스 메서드는 `Stock` 및 `DStock` 클래스 모두에서 올바르게 작동합니다. 이는 상속의 강력함을 보여주며, 동일한 메서드를 다른 하위 클래스에서 사용할 수 있습니다.

이 예제는 클래스 변수를 구성 메커니즘으로 사용하는 방법을 명확하게 보여줍니다. 하위 클래스는 메서드를 다시 작성하지 않고도 이러한 변수를 재정의하여 동작을 사용자 정의할 수 있습니다.

## 설계 토론

`__init__` 메서드에 유형 변환을 배치하는 대체 접근 방식을 고려해 보겠습니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

이 접근 방식을 사용하면 다음과 같이 데이터 행에서 `Stock` 객체를 만들 수 있습니다.

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

이 접근 방식이 처음에는 더 간단해 보일 수 있지만 몇 가지 단점이 있습니다.

1. 객체 초기화와 데이터 변환이라는 두 가지 다른 문제를 결합합니다. 이로 인해 코드를 이해하고 유지 관리하기가 더 어려워집니다.
2. `__init__` 메서드는 입력이 이미 올바른 유형인 경우에도 항상 입력을 변환하므로 덜 유연해집니다.
3. 하위 클래스가 변환 프로세스를 사용자 정의하는 방식을 제한합니다. 하위 클래스는 `__init__` 메서드에 포함된 경우 변환 로직을 변경하기가 더 어려워집니다.
4. 코드가 더 취약해집니다. 변환 중 하나라도 실패하면 객체를 생성할 수 없으므로 프로그램에서 오류가 발생할 수 있습니다.

반면에 클래스 메서드 접근 방식은 이러한 문제를 분리합니다. 이렇게 하면 코드의 각 부분이 단일 책임을 갖게 되므로 코드를 더 유지 관리하고 유연하게 만들 수 있습니다.
