# 클래스 변수와 클래스 메서드 이해하기

이 첫 번째 단계에서는 Python 의 클래스 변수와 클래스 메서드 개념에 대해 자세히 알아보겠습니다. 이는 보다 효율적이고 체계적인 코드를 작성하는 데 도움이 되는 중요한 개념입니다. 클래스 변수와 클래스 메서드를 사용하기 전에 먼저 `Stock` 클래스의 인스턴스가 현재 어떻게 생성되는지 살펴보겠습니다. 이를 통해 기본적인 이해를 얻고 개선할 수 있는 부분을 파악할 수 있습니다.

## 클래스 변수란 무엇인가요?

클래스 변수는 Python 에서 특별한 유형의 변수입니다. 클래스의 모든 인스턴스 간에 공유됩니다. 이를 더 잘 이해하기 위해 인스턴스 변수와 비교해 보겠습니다. 인스턴스 변수는 클래스의 각 인스턴스에 고유합니다. 예를 들어, 클래스의 여러 인스턴스가 있는 경우 각 인스턴스는 인스턴스 변수에 대한 자체 값을 가질 수 있습니다. 반면에 클래스 변수는 클래스 수준에서 정의됩니다. 즉, 해당 클래스의 모든 인스턴스가 클래스 변수의 동일한 값에 액세스하고 공유할 수 있습니다.

## 클래스 메서드란 무엇인가요?

클래스 메서드는 클래스의 개별 인스턴스가 아닌 클래스 자체에서 작동하는 메서드입니다. 클래스에 바인딩되어 있어 인스턴스를 생성하지 않고도 클래스에서 직접 호출할 수 있습니다. Python 에서 클래스 메서드를 정의하려면 `@classmethod` 데코레이터를 사용합니다. 그리고 인스턴스 (`self`) 를 첫 번째 매개변수로 사용하는 대신, 클래스 메서드는 클래스 (`cls`) 를 첫 번째 매개변수로 사용합니다. 이를 통해 클래스 수준의 데이터에서 작동하고 클래스 전체와 관련된 작업을 수행할 수 있습니다.

## 현재 Stock 인스턴스 생성 방식

먼저 현재 `Stock` 클래스의 인스턴스를 어떻게 생성하는지 살펴보겠습니다. 편집기에서 `stock.py` 파일을 열어 현재 구현을 확인하십시오.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

이 클래스의 인스턴스는 일반적으로 다음과 같은 방법 중 하나로 생성됩니다.

1. 값으로 직접 초기화:

   ```python
   s = Stock('GOOG', 100, 490.1)
   ```

   여기서는 `name`, `shares`, `price` 속성에 대한 값을 제공하여 `Stock` 클래스의 인스턴스를 직접 생성하고 있습니다. 이는 값을 미리 알고 있을 때 인스턴스를 생성하는 간단한 방법입니다.

2. CSV 파일에서 읽은 데이터로 생성:
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Skip the header
       row = next(rows)      # Get the first data row
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```
   CSV 파일에서 데이터를 읽을 때 값은 처음에 문자열 형식입니다. 따라서 CSV 데이터에서 `Stock` 인스턴스를 생성할 때 문자열 값을 적절한 유형으로 수동으로 변환해야 합니다. 예를 들어, `shares` 값은 정수로 변환해야 하고, `price` 값은 부동 소수점으로 변환해야 합니다.

이것을 시도해 봅시다. `~/project` 디렉토리에 다음 내용으로 `test_stock.py`라는 새 Python 파일을 만듭니다.

```python
# test_stock.py
from stock import Stock
import csv

# Method 1: Direct creation
s1 = Stock('GOOG', 100, 490.1)
print(f"Stock: {s1.name}, Shares: {s1.shares}, Price: {s1.price}")
print(f"Cost: {s1.cost()}")

# Method 2: Creation from CSV row
with open('portfolio.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip the header
    row = next(rows)      # Get the first data row
    s2 = Stock(row[0], int(row[1]), float(row[2]))
    print(f"\nStock from CSV: {s2.name}, Shares: {s2.shares}, Price: {s2.price}")
    print(f"Cost: {s2.cost()}")
```

이 파일을 실행하여 결과를 확인하십시오.

```bash
cd ~/project
python test_stock.py
```

다음과 유사한 출력이 표시되어야 합니다.

```
Stock: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0

Stock from CSV: AA, Shares: 100, Price: 32.2
Cost: 3220.0
```

이 수동 변환은 작동하지만 몇 가지 단점이 있습니다. 데이터의 정확한 형식을 알아야 하고 CSV 데이터에서 인스턴스를 생성할 때마다 변환을 수행해야 합니다. 이는 오류가 발생하기 쉽고 시간이 많이 걸릴 수 있습니다. 다음 단계에서는 클래스 메서드를 사용하여 더 우아한 솔루션을 만들 것입니다.
