# 프록시를 사용하여 읽기 전용 객체 만들기

이 단계에서는 Python 에서 매우 유용한 패턴인 프록시 클래스를 살펴보겠습니다. 프록시 클래스를 사용하면 원래 코드를 변경하지 않고 기존 객체의 동작 방식을 변경할 수 있습니다. 이는 객체 주위에 특수한 래퍼를 배치하여 새로운 기능이나 제한 사항을 추가하는 것과 같습니다.

## 프록시란 무엇인가?

프록시는 다른 객체와 여러분 사이에 있는 객체입니다. 원래 객체와 동일한 기능 및 속성 집합을 갖지만 추가 작업을 수행할 수 있습니다. 예를 들어, 객체에 접근할 수 있는 사람을 제어하고, 작업 기록 (로깅) 을 유지하거나, 기타 유용한 기능을 추가할 수 있습니다.

읽기 전용 프록시를 만들어 보겠습니다. 이러한 종류의 프록시는 객체의 속성을 변경하지 못하도록 합니다.

### 1 단계: 읽기 전용 프록시 클래스 만들기

먼저 읽기 전용 프록시를 정의하는 Python 파일을 만들어야 합니다.

1. `/home/labex/project` 디렉토리로 이동합니다.
2. 이 디렉토리에 `readonly_proxy.py`라는 새 파일을 만듭니다.
3. `readonly_proxy.py` 파일을 열고 다음 코드를 추가합니다.

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

이 코드에서는 `ReadonlyProxy` 클래스가 정의됩니다. `__init__` 메서드는 래핑하려는 객체를 저장합니다. `__setattr__` 메서드를 호출하지 않도록 직접 저장하기 위해 `self.__dict__`를 사용합니다. `__getattr__` 메서드는 프록시의 속성에 접근하려고 할 때 사용됩니다. 단순히 요청을 래핑된 객체로 전달합니다. `__setattr__` 메서드는 속성을 변경하려고 할 때 호출됩니다. 변경을 방지하기 위해 오류를 발생시킵니다.

### 2 단계: 테스트 파일 만들기

이제 읽기 전용 프록시가 어떻게 작동하는지 확인하기 위해 테스트 파일을 만들겠습니다.

1. 동일한 `/home/labex/project` 디렉토리에 `test_readonly.py`라는 새 파일을 만듭니다.
2. `test_readonly.py` 파일에 다음 코드를 추가합니다.

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

이 테스트 코드에서는 먼저 일반 `Stock` 객체를 만들고 해당 정보를 출력합니다. 그런 다음 해당 속성 중 하나를 수정하고 업데이트된 정보를 출력합니다. 다음으로, `Stock` 객체에 대한 읽기 전용 프록시를 만들고 해당 정보를 출력합니다. 마지막으로, 읽기 전용 프록시를 수정하려고 시도하고 오류가 발생할 것으로 예상합니다.

### 3 단계: 테스트 스크립트 실행

프록시 클래스와 테스트 파일을 만든 후에는 테스트 스크립트를 실행하여 결과를 확인해야 합니다.

1. 터미널을 열고 다음 명령을 사용하여 `/home/labex/project` 디렉토리로 이동합니다.

```bash
cd /home/labex/project
```

2. 다음 명령을 사용하여 테스트 스크립트를 실행합니다.

```bash
python3 test_readonly.py
```

다음과 유사한 출력이 표시됩니다.

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## 프록시 작동 방식

`ReadonlyProxy` 클래스는 읽기 전용 기능을 달성하기 위해 두 가지 특수 메서드를 사용합니다.

1. `__getattr__(self, name)`: 이 메서드는 Python 이 일반적인 방식으로 속성을 찾을 수 없을 때 호출됩니다. `ReadonlyProxy` 클래스에서는 `getattr()` 함수를 사용하여 속성 접근 요청을 래핑된 객체로 전달합니다. 따라서 프록시의 속성에 접근하려고 하면 실제로 래핑된 객체에서 속성을 가져옵니다.

2. `__setattr__(self, name, value)`: 이 메서드는 속성에 값을 할당하려고 할 때 호출됩니다. 구현에서는 `AttributeError`를 발생시켜 프록시의 속성에 대한 변경을 중지합니다.

3. `__init__` 메서드에서는 `self.__dict__`를 직접 수정하여 래핑된 객체를 저장합니다. 이는 객체를 할당하는 일반적인 방식을 사용하면 `__setattr__` 메서드가 호출되어 오류가 발생하기 때문에 중요합니다.

이 프록시 패턴을 사용하면 원래 클래스를 변경하지 않고 기존 객체 주위에 읽기 전용 계층을 추가할 수 있습니다. 프록시 객체는 래핑된 객체와 똑같이 작동하지만 변경을 할 수 없습니다.
