# 구조체 기본 클래스 생성하기

이제 함수 인자 전달에 대한 이해가 높아졌으므로, 데이터 구조에 재사용 가능한 기본 클래스를 만들 것입니다. 이 단계는 데이터를 저장하는 간단한 클래스를 만들 때 동일한 코드를 반복해서 작성하는 것을 피하는 데 도움이 되므로 매우 중요합니다. 기본 클래스를 사용하면 코드를 간소화하고 효율성을 높일 수 있습니다.

## 반복적인 코드의 문제점

이전 연습에서 아래와 같이 `Stock` 클래스를 정의했습니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

`__init__` 메서드를 자세히 살펴보십시오. 매우 반복적이라는 것을 알 수 있습니다. 각 속성을 하나씩 수동으로 할당해야 합니다. 이는 특히 많은 속성을 가진 많은 클래스가 있는 경우 매우 지루하고 시간이 많이 걸릴 수 있습니다.

## 유연한 기본 클래스 생성하기

속성 할당을 자동으로 처리할 수 있는 `Structure` 기본 클래스를 만들어 보겠습니다. 먼저 WebIDE 를 열고 `structure.py`라는 새 파일을 만듭니다. 그런 다음 이 파일에 다음 코드를 추가합니다.

```python
# structure.py

class Structure:
    """
    간단한 데이터 구조를 생성하기 위한 기본 클래스입니다.
    _fields 및 생성자 인자로부터 객체 속성을 자동으로 채웁니다.
    """
    _fields = ()

    def __init__(self, *args):
        # 인자 수가 _fields 의 수와 일치하는지 확인합니다.
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # 속성을 설정합니다.
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

이 기본 클래스에는 몇 가지 중요한 기능이 있습니다.

1.  `_fields` 클래스 변수를 정의합니다. 기본적으로 이 변수는 비어 있습니다. 이 변수는 클래스가 가질 속성의 이름을 저장합니다.
2.  생성자에 전달된 인자 수가 `_fields`에 정의된 필드 수와 일치하는지 확인합니다. 일치하지 않으면 `TypeError`를 발생시킵니다. 이는 오류를 조기에 감지하는 데 도움이 됩니다.
3.  필드 이름과 인자로 제공된 값을 사용하여 객체의 속성을 설정합니다. `setattr` 함수는 속성을 동적으로 설정하는 데 사용됩니다.

## 구조체 기본 클래스 테스트하기

이제 `Structure` 기본 클래스에서 상속하는 몇 가지 예제 클래스를 만들어 보겠습니다. `structure.py` 파일에 다음 코드를 추가합니다.

```python
# Structure 을 사용하는 예제 클래스
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

구현이 제대로 작동하는지 테스트하기 위해 `test_structure.py`라는 테스트 파일을 만들겠습니다. 이 파일에 다음 코드를 추가합니다.

```python
# test_structure.py
from structure import Stock, Point, Date

# Stock 클래스 테스트
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Point 클래스 테스트
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Date 클래스 테스트
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# 오류 처리 테스트
try:
    s2 = Stock('AAPL', 50)  # price 인자 누락
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

테스트를 실행하려면 터미널을 열고 다음 명령을 실행합니다.

```bash
python3 test_structure.py
```

다음 출력이 표시되어야 합니다.

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

보시다시피 기본 클래스가 예상대로 작동합니다. 동일한 상용구 코드를 반복해서 작성하지 않고도 새로운 데이터 구조를 정의하는 것이 훨씬 쉬워졌습니다.
