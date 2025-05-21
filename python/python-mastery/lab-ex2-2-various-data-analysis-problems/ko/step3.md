# collections 모듈 탐색

Python 에서 리스트, 딕셔너리, 세트와 같은 내장 컨테이너는 매우 유용합니다. 그러나 Python 의 `collections` 모듈은 이러한 내장 컨테이너의 기능을 확장하는 특수 컨테이너 데이터 유형을 제공하여 한 단계 더 나아갑니다. 이러한 유용한 데이터 유형 중 일부를 자세히 살펴보겠습니다.

Python 터미널에서 계속 작업하고 아래 예제를 따라 진행합니다.

## Counter

`Counter` 클래스는 딕셔너리의 하위 클래스입니다. 주요 목적은 해시 가능한 객체를 계산하는 것입니다. 항목을 계산하는 편리한 방법을 제공하며 다양한 작업을 지원합니다.

먼저 `Counter` 클래스와 포트폴리오를 읽는 함수를 가져와야 합니다. 그런 다음 CSV 파일에서 포트폴리오를 읽습니다.

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

이제 각 주식의 주식 수를 이름별로 계산하기 위해 `Counter` 객체를 만들겠습니다.

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

`Counter` 객체의 훌륭한 기능 중 하나는 새 키를 자동으로 0 으로 초기화한다는 것입니다. 즉, 카운트를 증가시키기 전에 키가 있는지 확인할 필요가 없으므로 카운트를 누적하는 코드가 단순화됩니다.

Counter 에는 특수 메서드도 함께 제공됩니다. 예를 들어, `most_common()` 메서드는 데이터 분석에 매우 유용합니다.

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

또한 산술 연산을 사용하여 카운터를 결합할 수 있습니다.

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict

`defaultdict`는 일반 딕셔너리와 유사하지만 고유한 기능이 있습니다. 아직 존재하지 않는 키에 대한 기본값을 제공합니다. 이렇게 하면 키를 사용하기 전에 키가 있는지 확인할 필요가 없으므로 코드를 단순화할 수 있습니다.

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

`defaultdict(list)`를 만들면 각 새 키에 대해 자동으로 새 빈 리스트가 생성됩니다. 따라서 키가 이전에 존재하지 않더라도 키의 값에 직접 추가할 수 있습니다. 이렇게 하면 키가 있는지 확인하고 빈 리스트를 수동으로 만들 필요가 없습니다.

다른 기본 팩토리 함수도 사용할 수 있습니다. 예를 들어 `int`, `float` 또는 사용자 정의 함수를 사용할 수 있습니다.

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

`collections` 모듈의 이러한 특수 컨테이너 유형은 데이터를 사용할 때 코드를 더 간결하고 효율적으로 만들 수 있습니다.
