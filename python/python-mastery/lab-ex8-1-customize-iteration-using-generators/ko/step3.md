# 반복 기능을 사용하여 클래스 향상시키기

이제 `Structure` 클래스와 하위 클래스가 반복을 지원하도록 만들었습니다. 반복은 Python 에서 항목 모음을 하나씩 반복할 수 있게 해주는 강력한 개념입니다. 클래스가 반복을 지원하면 더 유연해지고 많은 내장 Python 기능과 함께 작동할 수 있습니다. 이 반복 지원이 Python 에서 많은 강력한 기능을 어떻게 가능하게 하는지 살펴보겠습니다.

## 시퀀스 변환을 위한 반복 활용

Python 에는 `list()` 및 `tuple()`과 같은 내장 함수가 있습니다. 이러한 함수는 모든 반복 가능한 객체를 입력으로 사용할 수 있으므로 매우 유용합니다. 반복 가능한 객체는 목록, 튜플 또는 이제 `Structure` 클래스 인스턴스와 같이 반복할 수 있는 것입니다. `Structure` 클래스가 이제 반복을 지원하므로, 이를 쉽게 목록이나 튜플로 변환할 수 있습니다.

1. `Stock` 인스턴스로 이러한 작업을 시도해 보겠습니다. `Stock` 클래스는 `Structure`의 하위 클래스입니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

이 명령은 먼저 `Stock` 클래스를 가져오고, 해당 인스턴스를 생성한 다음, `list()` 및 `tuple()` 함수를 사용하여 이 인스턴스를 각각 목록과 튜플로 변환합니다. 출력은 인스턴스가 목록과 튜플로 표시되는 것을 보여줍니다.

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## 언패킹 (Unpacking)

Python 에는 언패킹이라는 매우 유용한 기능이 있습니다. 언패킹을 사용하면 반복 가능한 객체를 가져와 해당 요소를 한 번에 개별 변수에 할당할 수 있습니다. `Stock` 인스턴스는 반복 가능하므로 이 언패킹 기능을 사용할 수 있습니다.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

이 코드에서는 `Stock` 인스턴스를 생성한 다음 해당 요소를 `name`, `shares`, `price`의 세 가지 변수로 언패킹합니다. 그런 다음 이러한 변수를 출력합니다. 출력은 이러한 변수의 값을 보여줍니다.

```
Name: GOOG, Shares: 100, Price: 490.1
```

## 비교 기능 추가

클래스가 반복을 지원하면 비교 연산을 구현하기가 더 쉬워집니다. 비교 연산은 두 객체가 같은지 확인하는 데 사용됩니다. `Structure` 클래스에 `__eq__()` 메서드를 추가하여 인스턴스를 비교해 보겠습니다.

1. `structure.py` 파일을 다시 엽니다. `__eq__()` 메서드는 두 객체를 비교하기 위해 `==` 연산자를 사용할 때 호출되는 Python 의 특수 메서드입니다. `structure.py` 파일의 `Structure` 클래스에 다음 코드를 추가합니다.

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

이 메서드는 먼저 `isinstance()` 함수를 사용하여 `other` 객체가 `self`와 동일한 클래스의 인스턴스인지 확인합니다. 그런 다음 `self`와 `other`를 모두 튜플로 변환하고 이러한 튜플이 같은지 확인합니다.

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

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. `__eq__()` 메서드를 추가한 후 `structure.py` 파일을 저장합니다.

3. 비교 기능을 테스트해 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

이 코드는 세 개의 `Stock` 인스턴스 `a`, `b`, `c`를 생성합니다. 그런 다음 `==` 연산자를 사용하여 `a`를 `b`와, `a`를 `c`와 비교합니다. 출력은 이러한 비교의 결과를 보여줍니다.

```
a == b: True
a == c: False
```

4. 이제 모든 것이 제대로 작동하는지 확인하기 위해 단위 테스트를 실행해야 합니다. 단위 테스트는 프로그램의 서로 다른 부분이 예상대로 작동하는지 확인하는 코드 집합입니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 teststock.py
```

모든 것이 제대로 작동하면 테스트가 통과되었음을 나타내는 출력이 표시됩니다.

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

두 개의 간단한 메서드 (`__iter__()` 및 `__eq__()`) 만 추가하여 `Structure` 클래스를 더 Pythonic 하고 사용하기 쉽게 만드는 기능을 크게 향상시켰습니다.
