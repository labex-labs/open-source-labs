# 딕셔너리와 CSV 데이터 작업

주식 보유에 대한 간단한 데이터 세트를 검토하는 것으로 시작해 보겠습니다. 이 단계에서는 CSV 파일에서 데이터를 읽고 딕셔너리를 사용하여 구조화된 형식으로 저장하는 방법을 배우게 됩니다.

CSV (Comma-Separated Values, 쉼표로 구분된 값) 파일은 각 줄이 행을 나타내고 값이 쉼표로 구분되는 표 형식 데이터를 저장하는 일반적인 방법입니다. Python 의 딕셔너리는 키 - 값 쌍을 저장할 수 있는 강력한 데이터 구조입니다. 딕셔너리를 사용하면 CSV 파일의 데이터를 더 의미 있는 방식으로 구성할 수 있습니다.

먼저 다음 단계를 따라 WebIDE 에서 새 Python 파일을 만듭니다.

1. WebIDE 에서 "New File" 버튼을 클릭합니다.
2. 파일 이름을 `readport.py`로 지정합니다.
3. 다음 코드를 복사하여 파일에 붙여넣습니다.

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

이 코드는 몇 가지 중요한 작업을 수행하는 `read_portfolio` 함수를 정의합니다.

1. `filename` 매개변수로 지정된 CSV 파일을 엽니다. `open` 함수는 파일에 액세스하는 데 사용되며, `with` 문은 읽기를 완료한 후 파일이 제대로 닫히도록 합니다.
2. 헤더 행을 건너뜁니다. 헤더 행에는 일반적으로 CSV 파일의 열 이름이 포함되어 있습니다. `next(rows)`를 사용하여 반복자를 다음 행으로 이동하여 헤더를 효과적으로 건너뜁니다.
3. 각 데이터 행에 대해 딕셔너리를 만듭니다. 딕셔너리의 키는 'name', 'shares', 'price'입니다. 이러한 키는 데이터를 더 직관적인 방식으로 액세스하는 데 도움이 됩니다.
4. 주식을 정수로, 가격을 부동 소수점 숫자로 변환합니다. CSV 파일에서 읽은 데이터는 처음에 문자열 형식으로 되어 있으므로 계산을 위해 숫자 값이 필요하기 때문에 중요합니다.
5. 각 딕셔너리를 `portfolio`라는 목록에 추가합니다. 이 목록에는 CSV 파일의 모든 레코드가 포함됩니다.
6. 마지막으로, 딕셔너리의 전체 목록을 반환합니다.

이제 교통 데이터를 위한 파일을 만들어 보겠습니다. 다음 내용으로 `readrides.py`라는 새 파일을 만듭니다.

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

이 `read_rides_as_dicts` 함수는 `read_portfolio` 함수와 유사하게 작동합니다. CTA 버스 데이터와 관련된 CSV 파일을 읽고, 헤더 행을 건너뛰고, 각 데이터 행에 대한 딕셔너리를 만들고, 이러한 딕셔너리를 목록에 저장합니다.

이제 WebIDE 에서 터미널을 열어 `read_portfolio` 함수를 테스트해 보겠습니다.

1. "Terminal" 메뉴를 클릭하고 "New Terminal"을 선택합니다.
2. `python3`를 입력하여 Python 인터프리터를 시작합니다.
3. 다음 명령을 실행합니다.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

여기서는 `pprint` 함수 (pretty print) 를 사용하여 데이터를 더 읽기 쉬운 형식으로 표시합니다. 목록의 각 항목은 하나의 주식 보유를 나타내는 딕셔너리입니다. 딕셔너리에는 다음과 같은 키가 있습니다.

- 주식 기호 (`name`): 주식을 식별하는 데 사용되는 약어입니다.
- 보유 주식 수 (`shares`): 주식의 보유 주식 수를 나타냅니다.
- 주당 구매 가격 (`price`): 각 주식을 구매한 가격입니다.

'MSFT' 및 'IBM'과 같은 일부 주식이 여러 번 나타나는 것을 알 수 있습니다. 이는 동일한 주식의 서로 다른 구매를 나타내며, 서로 다른 시기와 가격으로 이루어졌을 수 있습니다.
