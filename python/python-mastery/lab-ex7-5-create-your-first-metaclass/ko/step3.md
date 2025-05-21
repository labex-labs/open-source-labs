# 메타클래스 사용하기

이제 상속을 통해 메타클래스를 사용하는 클래스를 생성해 보겠습니다. 이를 통해 클래스가 정의될 때 메타클래스가 어떻게 호출되는지 이해할 수 있습니다.

Python 에서 메타클래스는 다른 클래스를 생성하는 클래스입니다. 클래스를 정의하면 Python 은 메타클래스를 사용하여 해당 클래스 객체를 구성합니다. 상속을 사용하면 클래스가 사용할 메타클래스를 지정할 수 있습니다.

1. `mymeta.py`를 열고 파일 끝에 다음 코드를 추가합니다.

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

여기서는 `myobject`에서 상속하는 `Stock` 클래스를 정의하고 있습니다. `__init__` 메서드는 Python 클래스의 특수 메서드입니다. 클래스의 객체가 생성될 때 호출되며 객체의 속성을 초기화하는 데 사용됩니다. `cost` 메서드는 주식의 총 비용을 계산하고, `sell` 메서드는 주식 수를 줄입니다.

2. Ctrl+S 를 눌러 파일을 저장합니다. 파일을 저장하면 변경 사항이 저장되고 나중에 실행할 수 있습니다.

3. 이제 파일이 어떻게 되는지 확인하기 위해 실행해 보겠습니다. WebIDE 에서 터미널을 열고 다음을 실행합니다.

```bash
cd /home/labex/project
python3 mymeta.py
```

`cd` 명령은 현재 작업 디렉토리를 `/home/labex/project`로 변경하고, `python3 mymeta.py`는 Python 스크립트 `mymeta.py`를 실행합니다.

다음과 유사한 출력을 볼 수 있습니다.

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

이 출력은 `myobject` 및 `Stock` 클래스가 모두 생성될 때 메타클래스가 호출됨을 보여줍니다. 다음 사항에 유의하십시오.

- `Stock`의 경우 `Stock`이 `myobject`에서 상속받기 때문에 기본 클래스에 `myobject`가 포함됩니다.
- 속성 목록에는 정의한 모든 메서드 (`__init__`, `cost`, `sell`) 와 일부 기본 속성이 포함됩니다.

4. `Stock` 클래스와 상호 작용해 보겠습니다. 다음 내용으로 `test_stock.py`라는 새 파일을 만듭니다.

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

이 코드에서는 `mymeta` 모듈에서 `Stock` 클래스를 가져옵니다. 그런 다음 `apple`이라는 `Stock` 클래스의 인스턴스를 만듭니다. `Stock` 클래스의 메서드를 사용하여 주식에 대한 정보를 출력하고, 총 비용을 계산하고, 일부 주식을 판매한 다음 업데이트된 정보를 출력합니다.

5. `Stock` 클래스를 테스트하기 위해 이 파일을 실행합니다.

```bash
python3 test_stock.py
```

다음과 같은 출력을 볼 수 있습니다.

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

테스트 스크립트의 출력 전에 메타클래스 정보가 먼저 출력되는 것을 확인하십시오. 이는 메타클래스가 클래스가 정의될 때 호출되기 때문이며, 이는 테스트 스크립트의 코드가 실행되기 전에 발생합니다.
