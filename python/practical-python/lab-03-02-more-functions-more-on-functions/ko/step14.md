# 연습 3.4: 열 선택기 구축

많은 경우, CSV 파일의 모든 데이터가 아닌 선택된 열에만 관심이 있습니다. `parse_csv()` 함수를 수정하여 다음과 같이 사용자가 지정한 열을 선택적으로 선택할 수 있도록 합니다.

```python
>>> # Read all of the data
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]

>>> # Read only some of the data
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA', 'shares': '100'}, {'name': 'IBM', 'shares': '50'}, {'name': 'CAT', 'shares': '150'}, {'name': 'MSFT', 'shares': '200'}, {'name': 'GE', 'shares': '95'}, {'name': 'MSFT', 'shares': '50'}, {'name': 'IBM', 'shares': '100'}]
>>>
```

열 선택기의 예는 연습 2.23 에서 제공되었습니다. 그러나 이를 수행하는 한 가지 방법은 다음과 같습니다.

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

이 부분에는 몇 가지 까다로운 부분이 있습니다. 아마도 가장 중요한 것은 열 선택을 행 인덱스에 매핑하는 것입니다. 예를 들어, 입력 파일에 다음과 같은 헤더가 있다고 가정해 보겠습니다.

```python
>>> headers = ['name', 'date', 'time', 'shares', 'price']
>>>
```

이제 선택된 열이 다음과 같다고 가정해 보겠습니다.

```python
>>> select = ['name', 'shares']
>>>
```

적절한 선택을 수행하려면 선택된 열 이름을 파일의 열 인덱스에 매핑해야 합니다. 이것이 이 단계에서 수행하는 작업입니다.

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

다시 말해, "name"은 열 0 이고 "shares"는 열 3 입니다. 파일에서 데이터 행을 읽을 때, 인덱스는 이를 필터링하는 데 사용됩니다.

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
