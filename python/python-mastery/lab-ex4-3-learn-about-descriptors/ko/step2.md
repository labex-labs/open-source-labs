# 사용자 정의 Descriptor 생성

이 단계에서는 자체 descriptor 클래스를 생성합니다. 하지만 먼저 descriptor 가 무엇인지 이해해 보겠습니다. Descriptor 는 `__get__`, `__set__`, 그리고 `__delete__` 메서드로 구성된 descriptor 프로토콜을 구현하는 Python 객체입니다. 이러한 메서드를 통해 descriptor 는 속성 접근, 설정 및 삭제 방식을 관리할 수 있습니다. 자체 descriptor 클래스를 생성함으로써 이 프로토콜이 어떻게 작동하는지 더 잘 이해할 수 있습니다.

프로젝트 디렉토리에 `descrip.py`라는 새 파일을 생성합니다. 이 파일에는 사용자 정의 descriptor 클래스가 포함됩니다. 다음은 코드입니다.

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

`Descriptor` 클래스에서 `__init__` 메서드는 descriptor 를 이름으로 초기화합니다. `__get__` 메서드는 속성에 접근할 때 호출되고, `__set__` 메서드는 속성이 설정될 때 호출되며, `__delete__` 메서드는 속성이 삭제될 때 호출됩니다.

이제 사용자 정의 descriptor 를 실험하기 위한 테스트 파일을 생성해 보겠습니다. 이를 통해 descriptor 가 다양한 시나리오에서 어떻게 동작하는지 확인할 수 있습니다. 다음 코드를 사용하여 `test_descrip.py`라는 파일을 생성합니다.

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

`test_descrip.py` 파일에서 `descrip.py`에서 `Descriptor` 클래스를 가져옵니다. 그런 다음 세 개의 속성 `a`, `b`, 그리고 `c`를 가진 `Foo` 클래스를 생성하며, 각 속성은 descriptor 에 의해 관리됩니다. `Foo`의 인스턴스를 생성하고 속성 접근, 설정 및 삭제와 같은 작업을 수행하여 descriptor 메서드가 어떻게 호출되는지 확인합니다.

이제 이 테스트 파일을 실행하여 descriptor 가 작동하는 것을 살펴보겠습니다. 터미널을 열고 프로젝트 디렉토리로 이동한 다음 다음 명령을 사용하여 테스트 파일을 실행합니다.

```bash
cd ~/project
python3 test_descrip.py
```

다음과 같은 출력을 볼 수 있습니다.

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

보시다시피, descriptor 에 의해 관리되는 속성에 접근, 설정 또는 삭제할 때마다 해당 매직 메서드 (`__get__`, `__set__`, 또는 `__delete__`) 가 호출됩니다.

descriptor 를 대화형으로 살펴보겠습니다. 이를 통해 descriptor 를 실시간으로 테스트하고 결과를 즉시 확인할 수 있습니다. 터미널을 열고 프로젝트 디렉토리로 이동한 다음 `descrip.py` 파일을 사용하여 대화형 Python 세션을 시작합니다.

```bash
cd ~/project
python3 -i descrip.py
```

이제 대화형 Python 세션에서 다음 명령을 입력하여 descriptor 프로토콜이 어떻게 작동하는지 확인합니다.

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

여기서 핵심적인 통찰력은 descriptor 가 속성 접근을 가로채고 사용자 정의할 수 있는 방법을 제공한다는 것입니다. 이는 데이터 유효성 검사, 계산된 속성 및 기타 고급 동작을 구현하는 데 강력하게 해줍니다. Descriptor 를 사용하면 클래스 속성에 접근, 설정 및 삭제하는 방식을 더 잘 제어할 수 있습니다.
