# Stock 클래스 향상시키기

Python 에서 클래스는 데이터와 동작을 구성하는 강력한 방법입니다. 관련 데이터와 함수를 함께 그룹화할 수 있습니다. 이 섹션에서는 서식이 지정된 주식 정보를 표시하는 메서드를 추가하여 `Stock` 클래스를 향상시킬 것입니다. 이는 클래스에서 데이터와 동작을 모두 캡슐화하는 좋은 예입니다. 캡슐화는 데이터를 해당 데이터에 대해 작동하는 메서드와 함께 묶는 것을 의미하며, 이는 코드를 체계적으로 유지하고 관리하기 쉽게 만드는 데 도움이 됩니다.

1. 먼저 WebIDE 편집기에서 `stock.py` 파일을 열어야 합니다. `stock.py` 파일은 `Stock` 클래스 작업을 해온 곳입니다. 편집기에서 열면 클래스 정의를 변경할 수 있습니다.

2. 이제 새 `display()` 메서드를 추가하기 위해 `Stock` 클래스를 수정합니다. 이 메서드는 주식 정보를 보기 좋게 서식을 지정하여 출력하는 역할을 합니다. 방법은 다음과 같습니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

`__init__` 메서드에서는 주식 이름, 주식 수 및 가격을 초기화합니다. `cost` 메서드는 주식 수에 가격을 곱하여 주식의 총 비용을 계산합니다. 새로운 `display` 메서드는 f-string 을 사용하여 주식 정보 (이름, 주식 수, 가격 및 총 비용 포함) 의 서식을 지정하고 출력합니다.

3. 이러한 변경을 수행한 후에는 파일을 저장해야 합니다. 키보드에서 `Ctrl+S`를 누르거나 편집기에서 저장 아이콘을 클릭하여 이 작업을 수행할 수 있습니다. 파일을 저장하면 변경 사항이 유지되고 나중에 사용할 수 있습니다.

4. 다음으로, 새로운 Python 대화형 세션을 시작합니다. 대화형 세션을 사용하면 코드를 즉시 테스트할 수 있습니다. 세션을 시작하려면 터미널에서 다음 명령을 실행합니다.

```bash
python3 -i stock.py
```

`-i` 옵션은 `stock.py` 파일을 실행한 후 대화형 세션을 시작하도록 Python 에 지시합니다. 이렇게 하면 `Stock` 클래스와 해당 메서드를 즉시 사용할 수 있습니다.

5. 이제 주식 객체를 만들고 새 `display()` 메서드를 사용해 보겠습니다. Apple 주식을 나타내는 객체를 만든 다음 `display` 메서드를 호출하여 서식이 지정된 정보를 확인합니다. 코드는 다음과 같습니다.

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

대화형 세션에서 이 코드를 실행하면 다음과 같은 출력이 표시됩니다.

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

이 출력은 `display` 메서드가 올바르게 작동하고 주식 정보를 예상대로 서식을 지정하고 있음을 보여줍니다.

6. 마지막으로, 주식 목록을 만들고 모두 표시해 보겠습니다. 이를 통해 여러 주식 객체와 함께 `display` 메서드를 사용하는 방법을 보여줍니다. 코드는 다음과 같습니다.

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

이 코드를 실행하면 다음과 같은 출력이 표시됩니다.

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

`display()` 메서드를 클래스에 추가함으로써 서식 지정 로직을 클래스 자체 내에 캡슐화했습니다. 이렇게 하면 코드가 더 체계적이고 유지 관리하기 쉬워집니다. 주식 정보가 표시되는 방식을 변경해야 하는 경우 코드 전체에서 변경을 수행하는 대신 한 곳에서 `display` 메서드만 수정하면 됩니다.
