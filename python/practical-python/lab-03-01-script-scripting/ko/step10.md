# 타입 어노테이션 (Type Annotations)

함수 정의에 선택적인 타입 힌트 (type hint) 를 추가할 수도 있습니다.

```python
def read_prices(filename: str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

이 힌트는 작동상 아무런 영향을 미치지 않습니다. 이는 순전히 정보 제공을 위한 것입니다. 하지만 IDE, 코드 검사기 및 기타 도구에서 더 많은 작업을 수행하는 데 사용될 수 있습니다.

2 절에서, 주식 포트폴리오의 성과를 보여주는 보고서를 출력하는 `report.py`라는 프로그램을 작성했습니다. 이 프로그램은 몇 가지 함수로 구성되었습니다. 예를 들어:

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

하지만, 프로그램의 일부는 일련의 스크립트된 계산을 수행했습니다. 이 코드는 프로그램의 끝 부분 근처에 나타났습니다. 예를 들어:

```python
...

# Output the report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

이 연습에서는 이 프로그램을 가져와서 함수 사용을 중심으로 조금 더 강력하게 구성할 것입니다.
