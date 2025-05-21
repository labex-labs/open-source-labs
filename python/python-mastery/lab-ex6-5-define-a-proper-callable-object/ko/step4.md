# 챌린지: 호출 가능 객체를 메서드로 사용하기

Python 에서 클래스 내에서 호출 가능 객체 (callable object) 를 메서드로 사용할 때 해결해야 할 고유한 과제가 있습니다. 호출 가능 객체는 함수 자체 또는 `__call__` 메서드가 있는 객체와 같이 함수처럼 "호출"할 수 있는 것입니다. 클래스 메서드로 사용될 때 Python 이 인스턴스 (`self`) 를 첫 번째 인수로 전달하는 방식 때문에 예상대로 작동하지 않는 경우가 있습니다.

`Stock` 클래스를 생성하여 이 문제를 살펴보겠습니다. 이 클래스는 이름, 주식 수, 가격과 같은 속성을 가진 주식을 나타냅니다. 또한 작업 중인 데이터가 올바른지 확인하기 위해 validator 를 사용합니다.

먼저 `stock.py` 파일을 열어 `Stock` 클래스 작성을 시작합니다. 편집기에서 파일을 열려면 다음 명령을 사용할 수 있습니다.

```bash
code /home/labex/project/stock.py
```

이제 다음 코드를 `stock.py` 파일에 추가합니다. 이 코드는 주식의 속성을 초기화하는 `__init__` 메서드, 총 비용을 계산하는 `cost` 속성, 주식 수를 줄이는 `sell` 메서드를 사용하여 `Stock` 클래스를 정의합니다. 또한 `sell` 메서드에 대한 입력을 검증하기 위해 `ValidatedFunction`을 사용해 보겠습니다.

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

`Stock` 클래스를 정의한 후에는 예상대로 작동하는지 테스트해야 합니다. `test_stock.py`라는 테스트 파일을 만들고 다음 명령을 사용하여 엽니다.

```bash
code /home/labex/project/test_stock.py
```

다음 코드를 `test_stock.py` 파일에 추가합니다. 이 코드는 `Stock` 클래스의 인스턴스를 생성하고, 초기 주식 수와 비용을 출력하고, 일부 주식을 판매하려고 시도한 다음 업데이트된 주식 수와 비용을 출력합니다.

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

이제 다음 명령을 사용하여 테스트 파일을 실행합니다.

```bash
python3 /home/labex/project/test_stock.py
```

다음과 유사한 오류가 발생할 것입니다.

```
Error: missing a required argument: 'nshares'
```

이 오류는 Python 이 `s.sell(10)`과 같은 메서드를 호출할 때 실제로 내부적으로 `Stock.sell(s, 10)`을 호출하기 때문에 발생합니다. `self` 매개변수는 클래스의 인스턴스를 나타내며 자동으로 첫 번째 인수로 전달됩니다. 그러나 `ValidatedFunction`은 메서드로 사용되고 있음을 알지 못하므로 이 `self` 매개변수를 올바르게 처리하지 않습니다.

**문제 이해**

클래스 내에서 메서드를 정의한 다음 `ValidatedFunction`으로 바꾸면 본질적으로 원래 메서드를 래핑하는 것입니다. 문제는 래핑된 메서드가 `self` 매개변수를 자동으로 올바르게 처리하지 않는다는 것입니다. 인스턴스가 첫 번째 인수로 전달되는 것을 고려하지 않는 방식으로 인수를 예상합니다.

**문제 해결**

이 문제를 해결하려면 메서드를 처리하는 방식을 수정해야 합니다. 메서드 호출을 제대로 처리할 수 있는 `ValidatedMethod`라는 새 클래스를 만들 것입니다. 다음 코드를 `validate.py` 파일의 끝에 추가합니다.

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

이제 `ValidatedFunction` 대신 `ValidatedMethod`를 사용하도록 `Stock` 클래스를 수정해야 합니다. `stock.py` 파일을 다시 엽니다.

```bash
code /home/labex/project/stock.py
```

다음과 같이 `Stock` 클래스를 업데이트합니다.

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

`ValidatedMethod` 클래스는 속성이 액세스되는 방식을 변경할 수 있는 Python 의 특수한 유형의 객체인 descriptor 입니다. `__get__` 메서드는 속성이 메서드로 액세스될 때 호출됩니다. 인스턴스를 첫 번째 인수로 올바르게 전달하는 호출 가능 객체를 반환합니다.

다음 명령을 사용하여 테스트 파일을 다시 실행합니다.

```bash
python3 /home/labex/project/test_stock.py
```

이제 다음과 유사한 출력을 볼 수 있습니다.

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

이 챌린지는 호출 가능 객체의 중요한 측면을 보여주었습니다. 클래스에서 메서드로 사용할 때는 특별한 처리가 필요합니다. `__get__` 메서드를 사용하여 descriptor 프로토콜을 구현함으로써 독립 실행형 함수와 메서드 모두에서 올바르게 작동하는 호출 가능 객체를 만들 수 있습니다.
