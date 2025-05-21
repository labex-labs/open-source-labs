# 일반적인 객체 처리를 위한 getattr() 사용

`getattr()` 함수는 Python 에서 객체의 속성에 동적으로 접근할 수 있게 해주는 강력한 도구입니다. 이는 객체를 일반적인 방식으로 처리하려는 경우 특히 유용합니다. 특정 객체 유형에 특정한 코드를 작성하는 대신, `getattr()`을 사용하여 필요한 속성이 있는 모든 객체로 작업할 수 있습니다. 이러한 유연성은 코드를 더 재사용 가능하고 적응 가능하게 만듭니다.

## 여러 속성 처리

`getattr()` 함수를 사용하여 객체의 여러 속성에 접근하는 방법을 먼저 배우겠습니다. 이는 객체에서 특정 정보를 추출해야 할 때 일반적인 시나리오입니다.

먼저, 이전 셸을 닫았다면 Python 대화형 셸을 엽니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```python
# Open a Python interactive shell if you closed the previous one
python3
```

다음으로, `Stock` 클래스를 가져오고 `Stock` 객체를 생성합니다. `Stock` 클래스는 `name`, `shares`, `price`와 같은 속성을 가진 주식을 나타냅니다.

```python
# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

이제 접근하려는 속성 이름 목록을 정의합니다. 이 목록은 속성을 반복하고 해당 값을 출력하는 데 도움이 됩니다.

```python
# Define a list of attribute names
fields = ['name', 'shares', 'price']
```

마지막으로, `for` 루프를 사용하여 속성 이름 목록을 반복하고 `getattr()`을 사용하여 각 속성에 접근합니다. 각 반복에 대해 속성 이름과 해당 값을 출력합니다.

```python
# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

이 코드를 실행하면 다음과 같은 출력이 표시됩니다.

```
name: GOOG
shares: 100
price: 490.1
```

이 출력은 `getattr()` 함수를 사용하여 `Stock` 객체의 여러 속성의 값에 접근하고 출력할 수 있음을 보여줍니다.

## getattr() 을 사용한 기본값

`getattr()` 함수는 또한 유용한 기능을 제공합니다. 즉, 접근하려는 속성이 존재하지 않는 경우 기본값을 지정하는 기능입니다. 이는 코드에서 `AttributeError`가 발생하지 않도록 하고 코드를 더 강력하게 만들 수 있습니다.

이것이 어떻게 작동하는지 살펴보겠습니다. 먼저, `Stock` 객체에 존재하지 않는 속성에 접근하려고 합니다. `getattr()`을 사용하고 기본값 `'N/A'`를 제공합니다.

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

이 경우, `symbol` 속성이 `Stock` 객체에 존재하지 않으므로 `getattr()`은 기본값 `'N/A'`를 반환합니다.

이제 이것을 기존 속성에 접근하는 것과 비교해 보겠습니다. `Stock` 객체에 존재하는 `name` 속성에 접근합니다.

```python
# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

여기서 `getattr()`은 `name` 속성의 실제 값인 `'GOOG'`를 반환합니다.

## 객체 모음 처리

`getattr()` 함수는 객체 모음을 처리해야 할 때 더욱 강력해집니다. 이를 사용하여 주식 포트폴리오를 처리하는 방법을 살펴보겠습니다.

먼저, `stock` 모듈에서 `read_portfolio` 함수를 가져옵니다. 이 함수는 CSV 파일에서 주식 포트폴리오를 읽고 `Stock` 객체 목록을 반환합니다.

```python
# Import the portfolio reading function
from stock import read_portfolio
```

다음으로, `read_portfolio` 함수를 사용하여 `portfolio.csv`라는 CSV 파일에서 포트폴리오를 읽습니다.

```python
# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')
```

마지막으로, `for` 루프를 사용하여 포트폴리오의 `Stock` 객체 목록을 반복합니다. 각 주식에 대해 `getattr()`을 사용하여 `name` 및 `shares` 속성에 접근하고 해당 값을 출력합니다.

```python
# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

이 접근 방식은 속성 이름을 문자열로 사용할 수 있으므로 코드를 더 유연하게 만듭니다. 이러한 문자열은 인수로 전달되거나 데이터 구조에 저장될 수 있으므로 코드의 핵심 로직을 수정하지 않고도 접근하려는 속성을 쉽게 변경할 수 있습니다.
