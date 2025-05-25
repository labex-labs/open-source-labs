# 연습 문제 1.33: 명령줄에서 읽기 (Reading from the command line)

`pcost.py` 프로그램에서 입력 파일의 이름은 코드에 하드코딩되어 있습니다:

```python
# pcost.py

def portfolio_cost(filename):
    ...
    # Your code here
    ...

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)
```

이는 학습 및 테스트에는 괜찮지만, 실제 프로그램에서는 그렇게 하지 않을 것입니다.

대신, 스크립트에 인수로 파일 이름을 전달할 수 있습니다. 프로그램의 하단 부분을 다음과 같이 변경해 보십시오:

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header row
        for row in rows:
            if len(row) < 3:
                print("Skipping invalid row:", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Skipping invalid row:", row)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
```

`sys.argv`는 명령줄에서 전달된 인수 (있는 경우) 를 포함하는 목록입니다.

프로그램을 실행하려면 터미널에서 Python 을 실행해야 합니다.

예를 들어, Unix 의 bash 에서:

```bash
$ python3 pcost.py portfolio.csv
Total cost: 44671.15
bash %
```
