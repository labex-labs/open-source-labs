# 수동 클래스 생성

Python 프로그래밍에서 클래스는 데이터와 함수를 함께 그룹화할 수 있는 기본적인 개념입니다. 일반적으로 표준 Python 구문을 사용하여 클래스를 정의합니다. 예를 들어, 간단한 `Stock` 클래스가 있습니다. 이 클래스는 `name`, `shares`, `price`와 같은 속성을 가진 주식을 나타내며, 비용을 계산하고 주식을 판매하는 메서드를 가지고 있습니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

하지만 Python 이 실제로 어떻게 클래스를 내부적으로 생성하는지 궁금했던 적이 있습니까? 표준 클래스 구문을 사용하지 않고 이 클래스를 생성하려면 어떻게 해야 할까요? 이 섹션에서는 Python 클래스가 더 낮은 수준에서 어떻게 구성되는지 살펴보겠습니다.

## Python 대화형 셸 실행

수동 클래스 생성을 실험하려면 Python 대화형 셸을 열어야 합니다. 이 셸을 사용하면 Python 코드를 한 줄씩 실행할 수 있으며, 이는 학습 및 테스트에 매우 유용합니다.

WebIDE 에서 터미널을 열고 다음 명령을 입력하여 Python 대화형 셸을 시작합니다. 첫 번째 명령 `cd ~/project`는 현재 디렉토리를 프로젝트 디렉토리로 변경하고, 두 번째 명령 `python3`는 Python 3 대화형 셸을 시작합니다.

```bash
cd ~/project
python3
```

## 메서드를 일반 함수로 정의

클래스를 수동으로 생성하기 전에 클래스의 일부가 될 메서드를 정의해야 합니다. Python 에서 메서드는 클래스와 관련된 함수일 뿐입니다. 따라서 클래스에 원하는 메서드를 일반 Python 함수로 정의해 보겠습니다.

```python
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares
```

여기서 `__init__` 함수는 Python 클래스의 특수 메서드입니다. 생성자 (constructor) 라고 하며, 클래스의 인스턴스가 생성될 때 객체의 속성을 초기화하는 데 사용됩니다. `cost` 메서드는 주식의 총 비용을 계산하고, `sell` 메서드는 주식 수를 줄입니다.

## 메서드 딕셔너리 생성

이제 메서드를 일반 함수로 정의했으므로 클래스를 생성할 때 Python 이 이해할 수 있도록 메서드를 구성해야 합니다. 클래스의 모든 메서드를 포함하는 딕셔너리를 생성하여 이 작업을 수행합니다.

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

이 딕셔너리에서 키는 클래스에서 사용될 메서드의 이름이고, 값은 앞에서 정의한 실제 함수 객체입니다.

## `type()` 생성자를 사용하여 클래스 생성

Python 에서 `type()` 함수는 더 낮은 수준에서 클래스를 생성하는 데 사용할 수 있는 내장 함수입니다. `type()` 함수는 세 개의 인수를 사용합니다.

1. 클래스 이름: 생성하려는 클래스의 이름을 나타내는 문자열입니다.
2. 기본 클래스 튜플: Python 에서 클래스는 다른 클래스에서 상속받을 수 있습니다. 여기서는 `(object,)`를 사용하는데, 이는 클래스가 Python 의 모든 클래스의 기본 클래스인 기본 `object` 클래스에서 상속받는다는 의미입니다.
3. 메서드 및 속성을 포함하는 딕셔너리: 이것은 클래스의 모든 메서드를 담고 있는 앞에서 생성한 딕셔너리입니다.

```python
Stock = type('Stock', (object,), methods)
```

이 코드 줄은 `type()` 함수를 사용하여 `Stock`이라는 새 클래스를 생성합니다. 이 클래스는 `object` 클래스에서 상속받고 `methods` 딕셔너리에 정의된 메서드를 갖습니다.

## 수동으로 생성된 클래스 테스트

이제 클래스를 수동으로 생성했으므로 예상대로 작동하는지 테스트해 보겠습니다. 새 클래스의 인스턴스를 생성하고 해당 메서드를 호출합니다.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

첫 번째 줄에서 `GOOG`라는 이름, 100 주, 490.10 의 가격으로 `Stock` 클래스의 인스턴스를 생성합니다. 그런 다음 주식의 이름을 출력하고, 비용을 계산하여 출력하고, 25 주를 판매하고, 마지막으로 남은 주식 수를 출력합니다.

다음과 같은 출력이 표시됩니다.

```
GOOG
49010.0
75
```

이 출력은 수동으로 생성된 클래스가 표준 Python 구문을 사용하여 생성된 클래스와 마찬가지로 작동함을 보여줍니다. 이는 클래스가 기본적으로 이름, 기본 클래스 튜플, 메서드 및 속성의 딕셔너리임을 보여줍니다. `type()` 함수는 이러한 구성 요소에서 클래스 객체를 생성합니다.

작업이 완료되면 Python 셸을 종료합니다.

```python
exit()
```
