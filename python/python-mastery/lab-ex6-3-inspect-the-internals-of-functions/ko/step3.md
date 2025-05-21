# 클래스에서 함수 검사 적용

이제 함수 검사에 대해 배운 내용을 가져와 클래스 구현을 개선하는 데 사용해 보겠습니다. 함수 검사를 사용하면 함수 내부를 살펴보고 함수가 사용하는 매개변수와 같은 구조를 이해할 수 있습니다. 이 경우, 클래스 코드를 더 효율적이고 오류 발생 가능성이 적도록 만드는 데 사용합니다. `Structure` 클래스를 수정하여 `__init__` 메서드 시그니처에서 필드 이름을 자동으로 감지할 수 있도록 합니다.

## Structure 클래스 이해

`structure.py` 파일에는 `Structure` 클래스가 포함되어 있습니다. 이 클래스는 기본 클래스로 작동합니다. 즉, 다른 클래스가 이 클래스에서 상속받아 구조화된 데이터 객체를 만들 수 있습니다. 현재, `Structure`에서 상속받는 클래스에서 생성된 객체의 속성을 정의하려면 `_fields` 클래스 변수를 설정해야 합니다.

편집기에서 파일을 열어 보겠습니다. 다음 명령을 사용하여 프로젝트 디렉토리로 이동합니다.

```bash
cd ~/project
```

이 명령을 실행하면 WebIDE 내의 `structure.py` 파일에서 기존 `Structure` 클래스를 찾고 볼 수 있습니다.

## Stock 클래스 생성

`Structure` 클래스에서 상속받는 `Stock` 클래스를 만들어 보겠습니다. 상속은 `Stock` 클래스가 `Structure` 클래스의 모든 기능을 얻고 자체 기능을 추가할 수도 있음을 의미합니다. `structure.py` 파일의 끝에 다음 코드를 추가합니다.

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

그러나 이 접근 방식에는 문제가 있습니다. `_fields` 튜플과 `__init__` 메서드를 동일한 매개변수 이름으로 모두 정의해야 합니다. 이는 본질적으로 동일한 정보를 두 번 작성하고 있기 때문에 중복됩니다. 다른 항목을 변경할 때 하나를 업데이트하는 것을 잊으면 오류가 발생할 수 있습니다.

## set_fields 클래스 메서드 추가

이 문제를 해결하기 위해 `Structure` 클래스에 `set_fields` 클래스 메서드를 추가합니다. 이 메서드는 `__init__` 시그니처에서 필드 이름을 자동으로 감지합니다. `Structure` 클래스에 추가해야 하는 코드는 다음과 같습니다.

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

이 메서드는 Python 에서 함수 및 클래스와 같은 객체에 대한 정보를 얻는 데 강력한 도구인 `inspect` 모듈을 사용합니다. 먼저, `__init__` 메서드의 시그니처를 가져옵니다. 그런 다음, 매개변수 이름을 추출하지만 `self` 매개변수는 건너뜁니다. `self`는 인스턴스 자체를 참조하는 Python 클래스의 특수 매개변수이기 때문입니다. 마지막으로, 이러한 매개변수 이름으로 `_fields` 클래스 변수를 설정합니다.

## Stock 클래스 수정

이제 `set_fields` 메서드가 있으므로 `Stock` 클래스를 단순화할 수 있습니다. 이전 `Stock` 클래스 코드를 다음으로 바꿉니다.

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

이런 방식으로 `_fields` 튜플을 수동으로 정의할 필요가 없습니다. `set_fields` 메서드가 이를 처리합니다.

## 수정된 클래스 테스트

수정된 클래스가 제대로 작동하는지 확인하기 위해 간단한 테스트 스크립트를 만들겠습니다. `test_structure.py`라는 새 파일을 만들고 다음 코드를 추가합니다.

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

이 테스트 스크립트는 `Stock` 객체를 생성하고, 문자열 표현을 테스트하고, 속성에 액세스하고, 속성을 수정하고, 오타가 있는 속성에 액세스하여 올바른 오류가 발생하는지 확인합니다.

테스트 스크립트를 실행하려면 다음 명령을 사용합니다.

```bash
python3 test_structure.py
```

다음과 유사한 출력이 표시됩니다.

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## 작동 방식

1. `set_fields` 메서드는 `inspect.signature()`를 사용하여 `__init__` 메서드에서 매개변수 이름을 가져옵니다. 이 함수는 `__init__` 메서드의 매개변수에 대한 자세한 정보를 제공합니다.
2. 그런 다음, 이러한 매개변수 이름을 기반으로 `_fields` 클래스 변수를 자동으로 설정합니다. 따라서 동일한 매개변수 이름을 두 군데에 작성할 필요가 없습니다.
3. 이렇게 하면 일치하는 매개변수 이름으로 `_fields`와 `__init__`를 모두 수동으로 정의할 필요가 없어집니다. `__init__` 메서드의 매개변수를 변경하면 `_fields`가 자동으로 업데이트되므로 코드를 더 쉽게 유지 관리할 수 있습니다.

이 접근 방식은 함수 검사를 사용하여 코드를 더 쉽게 유지 관리하고 오류 발생 가능성을 줄입니다. 이는 런타임에 객체를 검사하고 수정할 수 있는 Python 의 인트로스펙션 (introspection) 기능을 실용적으로 적용한 것입니다.
