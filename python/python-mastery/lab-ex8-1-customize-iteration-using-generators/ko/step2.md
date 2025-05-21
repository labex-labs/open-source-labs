# 사용자 정의 클래스에 반복 추가하기

이제 제너레이터의 기본 사항을 이해했으므로, 이를 사용하여 사용자 정의 클래스에 반복 기능을 추가해 보겠습니다. Python 에서 클래스를 반복 가능하게 만들려면 `__iter__()` 특수 메서드를 구현해야 합니다. 반복 가능한 클래스를 사용하면 목록이나 튜플을 반복할 수 있는 것처럼 해당 요소들을 반복할 수 있습니다. 이는 사용자 정의 클래스를 더 유연하고 사용하기 쉽게 만드는 강력한 기능입니다.

## `__iter__()` 메서드 이해하기

`__iter__()` 메서드는 클래스를 반복 가능하게 만드는 데 중요한 부분입니다. 반복자 (iterator) 객체를 반환해야 합니다. 반복자는 반복 (루프) 할 수 있는 객체입니다. 이를 달성하는 간단하고 효과적인 방법은 `__iter__()`를 제너레이터 함수로 정의하는 것입니다. 제너레이터 함수는 `yield` 키워드를 사용하여 한 번에 하나씩 일련의 값을 생성합니다. `yield` 문이 나타날 때마다 함수는 일시 중지되고 값을 반환합니다. 다음 번에 반복자가 호출되면 함수는 중단된 지점부터 재개됩니다.

## Structure 클래스 수정하기

이 랩의 설정에서 기본 `Structure` 클래스를 제공했습니다. `Stock`과 같은 다른 클래스는 이 `Structure` 클래스에서 상속받을 수 있습니다. 상속은 기존 클래스의 속성과 메서드를 상속하는 새 클래스를 만드는 방법입니다. `Structure` 클래스에 `__iter__()` 메서드를 추가하면 모든 하위 클래스를 반복 가능하게 만들 수 있습니다. 즉, `Structure`에서 상속받는 모든 클래스는 자동으로 반복할 수 있는 기능을 갖게 됩니다.

1. WebIDE 에서 `structure.py` 파일을 엽니다.

```bash
cd ~/project
```

이 명령은 현재 작업 디렉토리를 `structure.py` 파일이 있는 `project` 디렉토리로 변경합니다. 파일을 액세스하고 수정하려면 올바른 디렉토리에 있어야 합니다.

2. `Structure` 클래스의 현재 구현을 살펴봅니다.

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

`Structure` 클래스에는 속성 이름을 저장하는 `_fields` 목록이 있습니다. `__init__()` 메서드는 클래스의 생성자입니다. 전달된 인수의 수가 필드 수와 같은지 확인하여 객체의 속성을 초기화합니다. 그렇지 않으면 `TypeError`를 발생시킵니다. 그렇지 않으면 `setattr()` 함수를 사용하여 속성을 설정합니다.

3. 각 속성 값을 순서대로 yield 하는 `__iter__()` 메서드를 추가합니다.

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

이 `__iter__()` 메서드는 제너레이터 함수입니다. `_fields` 목록을 반복하고 `getattr()` 함수를 사용하여 각 속성의 값을 가져옵니다. 그런 다음 `yield` 키워드는 값을 하나씩 반환합니다.

완전한 `structure.py` 파일은 이제 다음과 같이 표시됩니다.

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
```

이 업데이트된 `Structure` 클래스에는 `__iter__()` 메서드가 있어 이 클래스와 하위 클래스를 반복 가능하게 만듭니다.

4. 파일을 저장합니다.
   `structure.py` 파일을 변경한 후에는 변경 사항을 적용하기 위해 저장해야 합니다.

5. 이제 `Stock` 인스턴스를 생성하고 반복하여 반복 기능을 테스트해 보겠습니다.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

이 명령은 `Structure` 클래스에서 상속받는 `Stock` 클래스의 인스턴스를 생성합니다. 그런 다음 리스트 컴프리헨션을 사용하여 인스턴스를 반복하고 각 값을 출력합니다.

다음과 같은 출력을 볼 수 있습니다.

```
Iterating over Stock:
GOOG
100
490.1
```

이제 `Structure`에서 상속받는 모든 클래스는 자동으로 반복 가능하며, 반복은 `_fields` 목록에 정의된 순서대로 속성 값을 yield 합니다. 즉, 반복을 위해 추가 코드를 작성하지 않고도 `Structure`의 모든 하위 클래스의 속성을 쉽게 반복할 수 있습니다.
