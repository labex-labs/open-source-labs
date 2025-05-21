# Python 에서의 속성 접근 이해

Python 에서 객체는 기본적인 개념입니다. 객체는 값을 위한 명명된 컨테이너와 같은 속성에 데이터를 저장할 수 있습니다. 속성을 객체에 속하는 변수라고 생각할 수 있습니다. 이러한 속성에 접근하는 방법에는 여러 가지가 있습니다. 가장 간단하고 일반적으로 사용되는 방법은 점 (`.`) 표기법입니다. 그러나 Python 은 속성 작업 시 더 많은 유연성을 제공하는 특정 함수도 제공합니다.

## 점 표기법

`Stock` 객체를 생성하고 점 표기법을 사용하여 속성을 조작하는 방법을 살펴보겠습니다. 점 표기법은 객체의 속성에 접근하고 수정하는 간단하고 직관적인 방법입니다.

먼저, 새 터미널을 열고 Python 대화형 셸을 시작합니다. 여기에서 Python 코드를 한 줄씩 작성하고 실행할 수 있습니다.

```python
# Open a new terminal and run Python interactive shell
python3

# Import the Stock class from the stock module
from stock import Stock

# Create a Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(s.name)    # Output: 'GOOG'

# Set an attribute
s.shares = 50
print(s.shares)  # Output: 50

# Delete an attribute
del s.shares
# If we try to access s.shares now, we'll get an AttributeError
```

위 코드에서 먼저 `stock` 모듈에서 `Stock` 클래스를 가져옵니다. 그런 다음 `s`라는 `Stock` 클래스의 인스턴스를 생성합니다. `name` 속성의 값을 가져오려면 `s.name`을 사용합니다. `shares` 속성의 값을 변경하려면 단순히 `s.shares`에 새 값을 할당합니다. 그리고 속성을 제거하려면 `del` 키워드 다음에 속성 이름을 사용합니다.

## 속성 접근 함수

Python 은 속성 조작에 매우 유용한 네 가지 내장 함수를 제공합니다. 이러한 함수는 특히 속성을 동적으로 처리해야 할 때 속성 작업 시 더 많은 제어를 제공합니다.

1. `getattr()` - 이 함수는 속성의 값을 가져오는 데 사용됩니다.
2. `setattr()` - 속성의 값을 설정할 수 있습니다.
3. `delattr()` - 이 함수를 사용하여 속성을 삭제할 수 있습니다.
4. `hasattr()` - 이 함수는 객체에 속성이 있는지 확인합니다.

이러한 함수를 사용하는 방법을 살펴보겠습니다.

```python
# Create a new Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(getattr(s, 'name'))       # Output: 'GOOG'

# Set an attribute
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Check if an attribute exists
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Delete an attribute
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

이러한 함수는 특히 속성을 동적으로 작업해야 할 때 유용합니다. 하드 코딩된 속성 이름 대신 변수 이름을 사용할 수 있습니다. 예를 들어, 속성 이름을 저장하는 변수가 있는 경우 해당 변수를 이러한 함수에 전달하여 해당 속성에 대한 작업을 수행할 수 있습니다. 이를 통해 코드에서 더 많은 유연성을 얻을 수 있으며, 특히 다양한 객체와 속성을 보다 동적으로 처리할 때 유용합니다.
