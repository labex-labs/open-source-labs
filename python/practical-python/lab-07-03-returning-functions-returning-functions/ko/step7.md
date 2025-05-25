# 연습 문제 7.7: 클로저를 사용하여 중복 방지하기

클로저의 가장 강력한 기능 중 하나는 반복적인 코드를 생성하는 데 사용되는 것입니다. 연습 문제 5.7 로 돌아가서, 타입 검사를 사용하여 속성을 정의하는 코드를 기억해 보세요.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
    ...
```

이 코드를 반복해서 입력하는 대신, 클로저를 사용하여 자동으로 생성할 수 있습니다.

`typedproperty.py` 파일을 만들고 다음 코드를 넣으세요:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

이제 다음과 같이 클래스를 정의하여 사용해 보세요:

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

인스턴스를 생성하고 타입 검사가 작동하는지 확인해 보세요.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... should get a TypeError ...
>>>
```
