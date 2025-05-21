# 속성 제어를 위한 `__setattr__` 이해

Python 에는 객체의 속성에 접근하고 수정하는 방식을 사용자 정의할 수 있는 특수 메서드가 있습니다. 이러한 중요한 메서드 중 하나가 `__setattr__()`입니다. 이 메서드는 객체의 속성에 값을 할당하려고 할 때마다 실행됩니다. 이를 통해 속성 할당 프로세스를 세밀하게 제어할 수 있습니다.

## `__setattr__`란 무엇인가?

`__setattr__(self, name, value)` 메서드는 모든 속성 할당에 대한 인터셉터 역할을 합니다. `obj.attr = value`와 같은 간단한 할당 문을 작성하면 Python 은 단순히 값을 직접 할당하지 않습니다. 대신 내부적으로 `obj.__setattr__("attr", value)`를 호출합니다. 이 메커니즘은 속성 할당 중에 어떤 일이 발생해야 하는지 결정할 수 있는 권한을 제공합니다.

이제 `__setattr__`을 사용하여 클래스에서 설정할 수 있는 속성을 제한하는 실제 예제를 살펴보겠습니다.

### 1 단계: 새 파일 만들기

먼저 WebIDE 에서 새 파일을 엽니다. "File" 메뉴를 클릭한 다음 "New File"을 선택하여 이 작업을 수행할 수 있습니다. 이 파일의 이름을 `restricted_stock.py`로 지정하고 `/home/labex/project` 디렉토리에 저장합니다. 이 파일에는 `__setattr__`을 사용하여 속성 할당을 제어하는 클래스 정의가 포함됩니다.

### 2 단계: `restricted_stock.py`에 코드 추가

다음 코드를 `restricted_stock.py` 파일에 추가합니다. 이 코드는 `RestrictedStock` 클래스를 정의합니다.

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

`__init__` 메서드에서 `name`, `shares`, `price` 속성으로 객체를 초기화합니다. `__setattr__` 메서드는 할당되는 속성 이름이 허용된 속성 집합 (`name`, `shares`, `price`) 에 있는지 확인합니다. 그렇지 않은 경우 `AttributeError`를 발생시킵니다. 속성이 허용되면 상위 클래스의 `__setattr__` 메서드를 사용하여 실제로 속성을 설정합니다.

### 3 단계: 테스트 파일 만들기

`test_restricted.py`라는 새 파일을 만들고 다음 코드를 추가합니다. 이 코드는 `RestrictedStock` 클래스의 기능을 테스트합니다.

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

이 코드에서는 먼저 `RestrictedStock` 클래스를 가져옵니다. 그런 다음 클래스의 인스턴스를 만듭니다. 기존 속성에 접근하고, 기존 속성을 수정하고, 마지막으로 유효하지 않은 속성을 설정하여 `__setattr__` 메서드가 예상대로 작동하는지 테스트합니다.

### 4 단계: 테스트 파일 실행

WebIDE 에서 터미널을 열고 다음 명령을 실행하여 `test_restricted.py` 파일을 실행합니다.

```bash
cd /home/labex/project
python3 test_restricted.py
```

이러한 명령을 실행하면 다음과 유사한 출력이 표시됩니다.

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## 작동 방식

`RestrictedStock` 클래스의 `__setattr__` 메서드는 다음 단계로 작동합니다.

1. 먼저 속성 이름이 허용된 집합 (`name`, `shares`, `price`) 에 있는지 확인합니다.
2. 속성 이름이 허용된 집합에 없으면 `AttributeError`를 발생시킵니다. 이렇게 하면 원치 않는 속성이 할당되지 않습니다.
3. 속성이 허용되면 `super().__setattr__()`을 사용하여 실제로 속성을 설정합니다. 이렇게 하면 허용된 속성에 대해 정상적인 속성 할당 프로세스가 수행됩니다.

이 메서드는 이전 예제에서 살펴본 `__slots__`를 사용하는 것보다 더 유연합니다. `__slots__`는 메모리 사용량을 최적화하고 속성을 제한할 수 있지만 상속 작업 시 제한 사항이 있으며 다른 Python 기능과 충돌할 수 있습니다. `__setattr__` 접근 방식은 이러한 제한 사항 없이 속성 할당에 대한 유사한 제어를 제공합니다.
