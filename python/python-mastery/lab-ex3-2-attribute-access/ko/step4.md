# Python 에서 바운드 메서드 이해하기

Python 에서 메서드는 호출할 수 있는 특별한 유형의 속성입니다. 객체를 통해 메서드에 접근할 때, 우리는 이를 "바운드 메서드 (bound method)"라고 부릅니다. 바운드 메서드는 본질적으로 특정 객체에 연결된 메서드입니다. 즉, 객체의 데이터에 접근하여 해당 데이터를 조작할 수 있습니다.

## 속성으로 메서드 접근하기

`Stock` 클래스를 사용하여 바운드 메서드를 탐색해 보겠습니다. 먼저, 객체의 속성으로 메서드에 접근하는 방법을 살펴보겠습니다.

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

위 코드에서 먼저 `Stock` 클래스를 가져와서 인스턴스를 생성합니다. 그런 다음 실제로 호출하지 않고 `s` 객체의 `cost` 메서드에 접근합니다. 이렇게 하면 바운드 메서드가 생성됩니다. 이 바운드 메서드를 호출하면 객체의 데이터를 기반으로 비용을 계산합니다. 또한 한 단계로 객체에서 메서드를 직접 호출할 수도 있습니다.

## 메서드와 함께 getattr() 사용하기

메서드에 접근하는 또 다른 방법은 `getattr()` 함수를 사용하는 것입니다. 이 함수를 사용하면 이름으로 객체의 속성을 가져올 수 있습니다.

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

여기서는 `getattr()`을 사용하여 `s` 객체에서 `cost` 메서드를 가져옵니다. 이전과 마찬가지로 바운드 메서드를 호출하여 결과를 얻을 수 있습니다. 그리고 한 줄로 메서드를 가져와 호출할 수도 있습니다.

## 바운드 메서드와 해당 객체

바운드 메서드는 항상 접근한 객체에 대한 참조를 유지합니다. 즉, 메서드를 변수에 저장하더라도, 해당 메서드가 속한 객체를 알고 있으며 객체의 데이터에 접근할 수 있습니다.

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

이 예제에서는 `cost` 메서드를 변수 `c`에 저장합니다. `c()`를 호출하면 객체의 현재 데이터를 기반으로 비용을 계산합니다. 그런 다음 `s` 객체의 `shares` 속성을 변경합니다. `c()`를 다시 호출하면 업데이트된 데이터를 사용하여 새로운 비용을 계산합니다.

## 바운드 메서드 내부 탐색

바운드 메서드에는 이에 대한 더 많은 정보를 제공하는 두 가지 중요한 속성이 있습니다.

- `__self__`: 이 속성은 메서드가 바인딩된 객체를 참조합니다.
- `__func__`: 이 속성은 메서드를 나타내는 실제 함수 객체입니다.

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

여기서는 바운드 메서드 `c`의 `__self__` 및 `__func__` 속성에 접근합니다. `__self__`가 `s` 객체이고 `__func__`가 `cost` 함수임을 알 수 있습니다. 객체를 인수로 전달하여 함수를 수동으로 호출할 수도 있으며, 이는 바운드 메서드를 직접 호출하는 것과 동일한 결과를 제공합니다.

## 인수를 사용하는 메서드의 예

`sell()` 메서드와 같이 인수를 사용하는 메서드에서 바운드 메서드가 어떻게 작동하는지 살펴보겠습니다.

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

이 예제에서는 `sell` 메서드를 바운드 메서드로 가져옵니다. 인수를 사용하여 호출하면 `s` 객체의 `shares` 속성이 업데이트됩니다. 또한 `__func__` 및 `__self__` 속성을 사용하여 인수를 전달하여 메서드를 수동으로 호출할 수도 있습니다.

바운드 메서드를 이해하면 Python 의 객체 시스템이 내부적으로 어떻게 작동하는지 이해하는 데 도움이 되며, 이는 디버깅, 메타 프로그래밍 및 고급 프로그래밍 패턴을 만드는 데 유용할 수 있습니다.
