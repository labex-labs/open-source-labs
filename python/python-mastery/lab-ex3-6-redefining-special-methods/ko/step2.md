# `__eq__`를 사용하여 객체 비교 가능하게 만들기

Python 에서 두 객체를 비교하기 위해 `==` 연산자를 사용하면 Python 은 실제로 `__eq__` 특수 메서드를 호출합니다. 기본적으로 이 메서드는 객체의 id 를 비교합니다. 즉, 내용이 아닌 동일한 메모리 주소에 저장되어 있는지 확인합니다.

예를 들어 보겠습니다. `Stock` 클래스가 있고, 동일한 값을 가진 두 개의 `Stock` 객체를 생성한다고 가정해 보겠습니다. 그런 다음 `==` 연산자를 사용하여 비교하려고 합니다. Python 인터프리터에서 다음과 같이 할 수 있습니다.

먼저 터미널에서 다음 명령을 실행하여 Python 인터프리터를 시작합니다.

```bash
python3
```

그런 다음 Python 인터프리터에서 다음 코드를 실행합니다.

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

보시다시피, 두 `Stock` 객체 `a`와 `b`가 속성 (`name`, `shares`, `price`) 에 대해 동일한 값을 갖더라도 Python 은 서로 다른 메모리 위치에 저장되어 있기 때문에 서로 다른 객체로 간주합니다.

이 문제를 해결하기 위해 `Stock` 클래스에서 `__eq__` 메서드를 구현할 수 있습니다. 이 메서드는 `Stock` 클래스의 객체에 대해 `==` 연산자가 사용될 때마다 호출됩니다.

이제 `stock.py` 파일을 다시 엽니다. `Stock` 클래스 내부에 다음 `__eq__` 메서드를 추가합니다.

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

이 메서드가 수행하는 작업을 자세히 살펴보겠습니다.

1. 먼저 `isinstance` 함수를 사용하여 `other` 객체가 `Stock` 클래스의 인스턴스인지 확인합니다. 이는 `Stock` 객체만 다른 `Stock` 객체와 비교하려는 경우 중요합니다.
2. `other`가 `Stock` 객체인 경우, `self` 객체와 `other` 객체의 속성 (`name`, `shares`, `price`) 을 비교합니다.
3. 두 객체 모두 `Stock` 인스턴스이고 해당 속성이 동일한 경우에만 `True`를 반환합니다.

`__eq__` 메서드를 추가한 후, 완성된 `Stock` 클래스는 다음과 같이 표시됩니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

이제 개선된 `Stock` 클래스를 테스트해 보겠습니다. Python 인터프리터를 다시 시작합니다.

```bash
python3
```

그런 다음 Python 인터프리터에서 다음 코드를 실행합니다.

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

훌륭합니다! 이제 `Stock` 객체는 메모리 주소가 아닌 내용에 따라 제대로 비교할 수 있습니다.

`__eq__` 메서드의 `isinstance` 검사는 매우 중요합니다. 이는 `Stock` 객체만 비교하는지 확인합니다. 이 검사가 없으면 `Stock` 객체를 `Stock` 객체가 아닌 다른 것과 비교하면 오류가 발생할 수 있습니다.

테스트를 마쳤으면 다음 명령을 실행하여 Python 인터프리터를 종료할 수 있습니다.

```python
>>> exit()
```
