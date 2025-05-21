# 클래스 메서드에 데코레이터 적용하기

이제 데코레이터가 클래스 메서드와 어떻게 상호 작용하는지 살펴보겠습니다. Python 에는 인스턴스 메서드, 클래스 메서드, 정적 메서드 및 속성과 같은 다양한 유형의 메서드가 있기 때문에 약간 까다로울 수 있습니다. 데코레이터는 다른 함수를 가져와 명시적으로 수정하지 않고 후자 함수의 동작을 확장하는 함수입니다. 클래스 메서드에 데코레이터를 적용할 때는 이러한 다양한 메서드 유형과 데코레이터가 어떻게 작동하는지 주의해야 합니다.

## 문제 이해하기

`@logged` 데코레이터를 다양한 유형의 메서드에 적용할 때 어떤 일이 발생하는지 살펴보겠습니다. `@logged` 데코레이터는 메서드 호출에 대한 정보를 로깅하는 데 사용될 가능성이 높습니다.

1. WebIDE 에서 `methods.py`라는 새 파일을 만듭니다. 이 파일에는 `@logged` 데코레이터로 데코레이팅된 다양한 유형의 메서드가 있는 클래스가 포함됩니다.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

이 코드에는 네 가지 유형의 메서드가 있는 `Spam` 클래스가 있습니다. 각 메서드는 `@logged` 데코레이터로 데코레이팅되고, 일부는 `@classmethod`, `@staticmethod`, `@property`와 같은 다른 내장 데코레이터로도 데코레이팅됩니다.

2. 작동 방식을 테스트해 보겠습니다. 터미널에서 Python 명령을 실행하여 이러한 메서드를 호출하고 출력을 확인합니다.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

이 명령을 실행하면 몇 가지 문제가 발생할 수 있습니다.

- `@property` 데코레이터가 `@logged` 데코레이터와 제대로 작동하지 않을 수 있습니다. `@property` 데코레이터는 메서드를 속성으로 정의하는 데 사용되며 특정 방식으로 작동합니다. `@logged` 데코레이터와 결합하면 충돌이 발생할 수 있습니다.
- `@classmethod` 및 `@staticmethod`의 경우 데코레이터의 순서가 중요합니다. 데코레이터가 적용되는 순서에 따라 메서드의 동작이 변경될 수 있습니다.

## 데코레이터의 순서

여러 데코레이터를 적용하면 아래에서 위로 적용됩니다. 즉, 메서드 정의에 가장 가까운 데코레이터가 먼저 적용된 다음 그 위의 데코레이터가 순서대로 적용됩니다. 예를 들어:

```python
@decorator1
@decorator2
def func():
    pass
```

이는 다음과 같습니다.

```python
func = decorator1(decorator2(func))
```

이 예에서 `decorator2`가 먼저 `func`에 적용된 다음 `decorator1`이 `decorator2(func)`의 결과에 적용됩니다.

## 데코레이터 순서 수정하기

`methods.py` 파일을 업데이트하여 데코레이터 순서를 수정해 보겠습니다. 데코레이터의 순서를 변경하면 각 메서드가 예상대로 작동하도록 할 수 있습니다.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

이 업데이트된 버전에서:

- `instance_method`의 경우 순서는 중요하지 않습니다. 인스턴스 메서드는 클래스의 인스턴스에서 호출되며 `@logged` 데코레이터는 기본 기능에 영향을 주지 않고 어떤 순서로든 적용할 수 있습니다.
- `class_method`의 경우 `@logged` 다음에 `@classmethod`를 적용합니다. `@classmethod` 데코레이터는 메서드가 호출되는 방식을 변경하며, `@logged` 다음에 적용하면 로깅이 올바르게 작동하도록 합니다.
- `static_method`의 경우 `@logged` 다음에 `@staticmethod`를 적용합니다. `@classmethod`와 마찬가지로 `@staticmethod` 데코레이터는 자체 동작을 가지며 `@logged` 데코레이터와의 순서가 올바르게 지정되어야 합니다.
- `property_method`의 경우 `@logged` 다음에 `@property`를 적용합니다. 이렇게 하면 로깅 기능도 얻으면서 속성 동작이 유지됩니다.

3. 업데이트된 코드를 테스트해 보겠습니다. 이전과 동일한 명령을 실행하여 문제가 해결되었는지 확인합니다.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

이제 모든 메서드 유형에 대해 적절한 로깅을 볼 수 있습니다.

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## 메서드 데코레이터에 대한 모범 사례

메서드 데코레이터로 작업할 때는 다음 모범 사례를 따르십시오.

1. 메서드 변환 데코레이터 (`@classmethod`, `@staticmethod`, `@property`) 를 사용자 지정 데코레이터 **다음에** 적용합니다. 이렇게 하면 사용자 지정 데코레이터가 먼저 로깅 또는 기타 작업을 수행한 다음 내장 데코레이터가 의도한 대로 메서드를 변환할 수 있습니다.
2. 데코레이터 실행은 메서드 호출 시점이 아닌 클래스 정의 시점에 발생한다는 점을 인지하십시오. 즉, 데코레이터의 모든 설정 또는 초기화 코드는 메서드가 호출될 때가 아니라 클래스가 정의될 때 실행됩니다.
3. 더 복잡한 경우에는 서로 다른 메서드 유형에 대해 특수 데코레이터를 만들어야 할 수 있습니다. 서로 다른 메서드 유형은 서로 다른 동작을 가지며, 모든 경우에 적용되는 데코레이터는 모든 상황에서 작동하지 않을 수 있습니다.
