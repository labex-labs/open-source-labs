# Descriptor 프로토콜 이해

이 단계에서는 간단한 `Stock` 클래스를 생성하여 Python 에서 descriptor 가 어떻게 작동하는지 배우겠습니다. Python 의 descriptor 는 속성 접근, 설정 및 삭제 방식을 사용자 정의할 수 있는 강력한 기능입니다. Descriptor 프로토콜은 `__get__()`, `__set__()`, 그리고 `__delete__()`의 세 가지 특수 메서드로 구성됩니다. 이 메서드는 각각 속성에 접근, 값을 할당 또는 삭제할 때 descriptor 가 어떻게 동작하는지 정의합니다.

먼저, 프로젝트 디렉토리에 `stock.py`라는 새 파일을 생성해야 합니다. 이 파일에는 `Stock` 클래스가 포함됩니다. 다음은 `stock.py` 파일에 넣어야 할 코드입니다.

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

이 `Stock` 클래스에서는 `property` 데코레이터를 사용하여 `name`, `shares`, 그리고 `price` 속성에 대한 getter 및 setter 메서드를 정의하고 있습니다. 이러한 getter 및 setter 메서드는 descriptor 역할을 하며, 이는 이러한 속성에 접근하고 설정하는 방식을 제어한다는 의미입니다. 예를 들어, setter 메서드는 입력 값이 올바른 유형이고 허용 가능한 범위 내에 있는지 확인하기 위해 입력 값을 검증합니다.

이제 `stock.py` 파일이 준비되었으므로, Python 셸을 열어 `Stock` 클래스를 실험하고 descriptor 가 실제로 어떻게 작동하는지 살펴보겠습니다. 이렇게 하려면 터미널을 열고 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -i stock.py
```

`python3` 명령의 `-i` 옵션은 `stock.py` 파일을 실행한 후 대화형 셸을 시작하도록 Python 에 지시합니다. 이렇게 하면 방금 정의한 `Stock` 클래스와 직접 상호 작용할 수 있습니다.

Python 셸에서 주식 객체를 생성하고 해당 속성에 접근해 보겠습니다. 다음은 그 방법입니다.

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

`s` 객체의 `name` 및 `shares` 속성에 접근하면 Python 은 실제로 descriptor 의 `__get__` 메서드를 내부적으로 사용합니다. 클래스의 `property` 데코레이터는 descriptor 를 사용하여 구현되므로, 속성의 접근 및 할당을 제어된 방식으로 처리합니다.

클래스 사전을 자세히 살펴보고 descriptor 객체를 살펴보겠습니다. 클래스 사전에는 클래스에 정의된 모든 속성과 메서드가 포함되어 있습니다. 다음 코드를 사용하여 클래스 사전의 키를 볼 수 있습니다.

```python
Stock.__dict__.keys()
```

다음과 유사한 출력을 볼 수 있습니다.

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

`name`, `shares`, 그리고 `price` 키는 `property` 데코레이터에 의해 생성된 descriptor 객체를 나타냅니다.

이제 descriptor 가 어떻게 작동하는지 수동으로 메서드를 호출하여 살펴보겠습니다. `shares` descriptor 를 예로 사용하겠습니다. 다음은 그 방법입니다.

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

`s.shares`와 같은 속성에 접근하면 Python 은 descriptor 의 `__get__` 메서드를 호출하여 값을 검색합니다. `s.shares = 75`와 같이 값을 할당하면 Python 은 descriptor 의 `__set__` 메서드를 호출합니다. 그러면 descriptor 는 데이터를 검증하고 입력 값이 유효하지 않은 경우 오류를 발생시킬 수 있습니다.

`Stock` 클래스와 descriptor 를 실험하는 것을 마치면 다음 명령을 실행하여 Python 셸을 종료할 수 있습니다.

```python
exit()
```
