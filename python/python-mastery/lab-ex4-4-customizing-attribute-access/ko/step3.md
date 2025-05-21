# 상속의 대안으로서의 위임 (Delegation)

객체 지향 프로그래밍에서 코드를 재사용하고 확장하는 것은 일반적인 작업입니다. 이를 달성하는 두 가지 주요 방법은 상속과 위임입니다.

**상속 (Inheritance)**은 하위 클래스가 상위 클래스에서 메서드와 속성을 상속받는 메커니즘입니다. 하위 클래스는 자체 구현을 제공하기 위해 이러한 상속된 메서드 중 일부를 재정의하도록 선택할 수 있습니다.

반면에 **위임 (Delegation)**은 다른 객체를 포함하고 특정 메서드 호출을 해당 객체로 전달하는 객체를 포함합니다.

이 단계에서는 상속의 대안으로 위임을 살펴보겠습니다. 일부 동작을 다른 객체에 위임하는 클래스를 구현할 것입니다.

## 위임 예제 설정

먼저 위임 클래스가 상호 작용할 기본 클래스를 설정해야 합니다.

1. `/home/labex/project` 디렉토리에 `base_class.py`라는 새 파일을 만듭니다. 이 파일은 `method_a`, `method_b`, `method_c`의 세 가지 메서드를 가진 `Spam`이라는 클래스를 정의합니다. 각 메서드는 메시지를 출력하고 결과를 반환합니다. 다음은 `base_class.py`에 넣을 코드입니다.

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

다음으로 위임 클래스를 만들겠습니다.

2. `delegator.py`라는 새 파일을 만듭니다. 이 파일에서는 동작의 일부를 `Spam` 클래스의 인스턴스에 위임하는 `DelegatingSpam`이라는 클래스를 정의합니다.

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

`__init__` 메서드에서 `Spam` 클래스의 인스턴스를 만듭니다. `method_a` 메서드는 원래 메서드를 재정의하지만 `Spam` 클래스의 `method_a`도 호출합니다. `method_c` 메서드는 원래 메서드를 완전히 재정의합니다. `__getattr__` 메서드는 `DelegatingSpam` 클래스에 존재하지 않는 속성 또는 메서드에 접근할 때 호출되는 Python 의 특수 메서드입니다. 그런 다음 호출을 `Spam` 인스턴스에 위임합니다.

이제 구현을 확인하기 위해 테스트 파일을 만들어 보겠습니다.

3. `test_delegation.py`라는 테스트 파일을 만듭니다. 이 파일은 `DelegatingSpam` 클래스의 인스턴스를 만들고 해당 메서드를 호출합니다.

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

마지막으로 테스트 스크립트를 실행합니다.

4. 터미널에서 다음 명령을 사용하여 테스트 스크립트를 실행합니다.

```bash
cd /home/labex/project
python3 test_delegation.py
```

다음과 유사한 출력이 표시됩니다.

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## 위임 vs. 상속

이제 위임을 전통적인 상속과 비교해 보겠습니다.

1. `inheritance_example.py`라는 파일을 만듭니다. 이 파일에서는 `Spam` 클래스에서 상속하는 `InheritingSpam`이라는 클래스를 정의합니다.

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

`InheritingSpam` 클래스는 `method_a` 및 `method_c` 메서드를 재정의합니다. `method_a` 메서드에서는 `super()`를 사용하여 상위 클래스의 `method_a`를 호출합니다.

다음으로 상속 예제에 대한 테스트 파일을 만들겠습니다.

2. `test_inheritance.py`라는 테스트 파일을 만듭니다. 이 파일은 `InheritingSpam` 클래스의 인스턴스를 만들고 해당 메서드를 호출합니다.

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

마지막으로 상속 테스트를 실행합니다.

3. 터미널에서 다음 명령을 사용하여 상속 테스트를 실행합니다.

```bash
cd /home/labex/project
python3 test_inheritance.py
```

다음과 유사한 출력이 표시됩니다.

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## 주요 차이점 및 고려 사항

위임과 상속의 유사점과 차이점을 살펴보겠습니다.

1. **메서드 재정의**: 위임과 상속 모두 메서드를 재정의할 수 있지만 구문이 다릅니다.

   - 위임에서는 자체 메서드를 정의하고 래핑된 객체의 메서드를 호출할지 여부를 결정합니다.
   - 상속에서는 자체 메서드를 정의하고 `super()`를 사용하여 상위 메서드를 호출합니다.

2. **메서드 접근**:

   - 위임에서는 정의되지 않은 메서드가 `__getattr__` 메서드를 통해 전달됩니다.
   - 상속에서는 정의되지 않은 메서드가 자동으로 상속됩니다.

3. **유형 관계**:

   - 위임을 사용하면 `isinstance(delegating_spam, Spam)`은 `False`를 반환합니다. `DelegatingSpam` 객체가 `Spam` 클래스의 인스턴스가 아니기 때문입니다.
   - 상속을 사용하면 `isinstance(inheriting_spam, Spam)`은 `True`를 반환합니다. `InheritingSpam` 클래스가 `Spam` 클래스에서 상속되기 때문입니다.

4. **제한 사항**: `__getattr__`를 통한 위임은 `__getitem__`, `__len__` 등과 같은 특수 메서드에서는 작동하지 않습니다. 이러한 메서드는 위임 클래스에서 명시적으로 정의해야 합니다.

위임은 다음과 같은 상황에서 특히 유용합니다.

- 계층 구조에 영향을 주지 않고 객체의 동작을 사용자 정의하려는 경우.
- 공통 상위 항목을 공유하지 않는 여러 객체의 동작을 결합하려는 경우.
- 상속이 제공하는 것보다 더 많은 유연성이 필요한 경우.

상속은 일반적으로 다음과 같은 경우에 선호됩니다.

- "is-a" 관계가 명확한 경우 (예: Car 는 Vehicle 임).
- 코드 전체에서 유형 호환성을 유지해야 하는 경우.
- 특수 메서드를 상속해야 하는 경우.
