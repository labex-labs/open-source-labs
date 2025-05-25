# 연습 문제 2.4: 튜플의 리스트

`portfolio.csv` 파일에는 포트폴리오에 있는 주식 목록이 포함되어 있습니다. 연습 문제 1.30 에서 이 파일을 읽고 간단한 계산을 수행하는 함수 `portfolio_cost(filename)`을 작성했습니다.

작성한 코드는 다음과 유사해야 합니다.

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

이 코드를 대략적인 가이드로 사용하여 새 파일 `report.py`를 만듭니다. 해당 파일에서 주어진 포트폴리오 파일을 열어 튜플의 리스트로 읽어 들이는 함수 `read_portfolio(filename)`을 정의합니다. 이렇게 하려면 위의 코드에 몇 가지 사소한 수정을 해야 합니다.

먼저, `total_cost = 0`을 정의하는 대신, 처음에는 빈 리스트로 설정된 변수를 만듭니다. 예를 들어:

```python
portfolio = []
```

다음으로, 비용을 합산하는 대신, 각 행을 바로 이전 연습에서 했던 것처럼 튜플로 변환하고 이 리스트에 추가합니다. 예를 들어:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

마지막으로, 결과 `portfolio` 리스트를 반환합니다.

함수를 대화형으로 실험해 보십시오 (이 작업을 수행하려면 먼저 인터프리터에서 `report.py` 프로그램을 실행해야 함을 다시 한 번 상기시켜 드립니다).

_힌트: 터미널에서 파일을 실행할 때 `-i`를 사용하십시오._

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

이렇게 생성한 튜플의 리스트는 2 차원 배열과 매우 유사합니다. 예를 들어, `portfolio[row][column]`과 같은 조회를 사용하여 특정 열과 행에 접근할 수 있습니다. 여기서 `row`와 `column`은 정수입니다.

즉, 다음과 같은 문을 사용하여 마지막 for 루프를 다시 작성할 수도 있습니다.

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
