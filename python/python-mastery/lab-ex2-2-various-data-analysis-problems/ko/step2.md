# 리스트, 세트 및 딕셔너리 컴프리헨션 사용

Python 컴프리헨션은 기존 컬렉션을 기반으로 새로운 컬렉션을 만드는 매우 유용하고 간결한 방법입니다. Python 의 컬렉션은 리스트, 세트 또는 딕셔너리가 될 수 있으며, 이는 다양한 유형의 데이터를 담는 컨테이너와 같습니다. 컴프리헨션을 사용하면 특정 데이터를 필터링하고, 데이터를 어떤 방식으로 변환하고, 보다 효율적으로 구성할 수 있습니다. 이 부분에서는 포트폴리오 데이터를 사용하여 이러한 컴프리헨션이 어떻게 작동하는지 살펴보겠습니다.

먼저 이전 단계에서 했던 것처럼 Python 터미널을 열어야 합니다. 터미널이 열리면 다음 예제를 하나씩 입력합니다. 이러한 실습 방식은 컴프리헨션이 실제로 어떻게 작동하는지 이해하는 데 도움이 됩니다.

## 리스트 컴프리헨션

리스트 컴프리헨션은 Python 에서 새로운 리스트를 만드는 특수한 구문입니다. 기존 컬렉션의 각 항목에 표현식을 적용하여 수행합니다.

예시부터 시작해 보겠습니다. 먼저 포트폴리오 데이터를 읽는 함수를 가져오겠습니다. 그런 다음 리스트 컴프리헨션을 사용하여 포트폴리오에서 특정 보유 자산을 필터링합니다.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

이 코드에서 먼저 `read_portfolio` 함수를 가져와 CSV 파일에서 포트폴리오 데이터를 읽는 데 사용합니다. 그런 다음 리스트 컴프리헨션 `[s for s in portfolio if s['shares'] > 100]`은 `portfolio` 컬렉션의 각 항목 `s`를 거칩니다. 해당 보유 자산의 주식 수가 100 보다 큰 경우에만 새 리스트 `large_holdings`에 항목 `s`를 포함합니다.

리스트 컴프리헨션은 계산을 수행하는 데에도 사용할 수 있습니다. 다음은 몇 가지 예입니다.

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

첫 번째 예에서 리스트 컴프리헨션 `[s['shares'] * s['price'] for s in portfolio]`는 `portfolio`의 각 항목에 대해 주식 수에 가격을 곱하여 각 보유 자산의 총 비용을 계산합니다. 두 번째 예에서는 `sum` 함수를 리스트 컴프리헨션과 함께 사용하여 전체 포트폴리오의 총 비용을 계산합니다.

## 세트 컴프리헨션

세트 컴프리헨션은 기존 컬렉션에서 세트를 만드는 데 사용됩니다. 세트는 고유한 값만 포함하는 컬렉션입니다.

포트폴리오 데이터로 어떻게 작동하는지 살펴보겠습니다.

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

이 코드에서 세트 컴프리헨션 `{s['name'] for s in portfolio}`는 `portfolio`의 각 항목 `s`를 거쳐 주식 이름 (`s['name']`) 을 세트 `unique_stocks`에 추가합니다. 세트는 고유한 값만 저장하므로 중복 없이 포트폴리오의 모든 다른 주식 목록이 생성됩니다.

## 딕셔너리 컴프리헨션

딕셔너리 컴프리헨션은 표현식을 적용하여 키 - 값 쌍을 생성하여 새로운 딕셔너리를 만듭니다.

다음은 딕셔너리 컴프리헨션을 사용하여 포트폴리오의 각 주식에 대한 총 주식 수를 계산하는 예입니다.

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

첫 번째 줄에서 딕셔너리 컴프리헨션 `{s['name']: 0 for s in portfolio}`는 각 주식 이름 (`s['name']`) 이 키이고 각 키의 초기 값이 0 인 딕셔너리를 만듭니다. 그런 다음 `for` 루프를 사용하여 `portfolio`의 각 항목을 거칩니다. 각 항목에 대해 주식 수 (`s['shares']`) 를 `totals` 딕셔너리의 해당 값에 추가합니다.

이러한 컴프리헨션은 단 몇 줄의 코드로 데이터를 변환하고 분석할 수 있으므로 매우 강력합니다. Python 프로그래밍 도구 상자에 포함할 수 있는 훌륭한 도구입니다.
