# `__repr__`을 사용한 객체 표현 개선

Python 에서 객체는 두 가지 방식으로 문자열로 표현될 수 있습니다. 이러한 표현은 서로 다른 목적을 가지며 다양한 시나리오에서 유용합니다.

첫 번째 유형은 **문자열 표현 (string representation)**입니다. 이는 `str()` 함수에 의해 생성되며, `print()` 함수를 사용할 때 자동으로 호출됩니다. 문자열 표현은 사람이 읽을 수 있도록 설계되었습니다. 객체를 우리가 이해하고 해석하기 쉬운 형식으로 나타냅니다.

두 번째 유형은 **코드 표현 (code representation)**입니다. 이는 `repr()` 함수에 의해 생성됩니다. 코드 표현은 객체를 다시 생성하기 위해 작성해야 하는 코드를 보여줍니다. 이는 코드에서 객체를 정확하고 모호하지 않게 표현하는 데 더 중점을 둡니다.

Python 의 내장 `date` 클래스를 사용하여 구체적인 예를 살펴보겠습니다. 이를 통해 문자열 표현과 코드 표현의 차이점을 실제로 확인할 수 있습니다.

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

이 예에서 `print(d)`를 사용하면 Python 은 `date` 객체 `d`에 대해 `str()` 함수를 호출하고, `YYYY-MM-DD` 형식의 사람이 읽을 수 있는 날짜를 얻습니다. 대화형 셸에서 단순히 `d`를 입력하면 Python 은 `repr()` 함수를 호출하고, `date` 객체를 다시 생성하는 데 필요한 코드를 볼 수 있습니다.

다양한 방법으로 `repr()` 문자열을 명시적으로 얻을 수 있습니다. 다음은 몇 가지 예입니다.

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

이제 이 개념을 `Stock` 클래스에 적용해 보겠습니다. `__repr__` 메서드를 구현하여 클래스를 개선할 것입니다. 이 특수 메서드는 객체의 코드 표현이 필요할 때 Python 에서 호출됩니다.

이를 위해 편집기에서 `stock.py` 파일을 엽니다. 그런 다음 `__repr__` 메서드를 `Stock` 클래스에 추가합니다. `__repr__` 메서드는 `Stock` 객체를 다시 생성하는 데 필요한 코드를 보여주는 문자열을 반환해야 합니다.

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

`__repr__` 메서드를 추가한 후, 완성된 `Stock` 클래스는 다음과 같이 표시됩니다.

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
```

이제 수정된 `Stock` 클래스를 테스트해 보겠습니다. 터미널에서 다음 명령을 실행하여 Python 대화형 셸을 엽니다.

```bash
python3
```

대화형 셸이 열리면 다음 명령을 시도해 보십시오.

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

`__repr__` 메서드가 주식 포트폴리오와 어떻게 작동하는지 확인할 수도 있습니다. 다음은 예입니다.

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

보시다시피, `__repr__` 메서드는 대화형 셸 또는 디버거에 표시될 때 `Stock` 객체를 훨씬 더 유익하게 만들었습니다. 이제 각 객체를 다시 생성하는 데 필요한 코드를 표시하므로 디버깅 및 객체의 상태를 이해하는 데 매우 유용합니다.

테스트를 마쳤으면 다음 명령을 실행하여 Python 인터프리터를 종료할 수 있습니다.

```python
>>> exit()
```
