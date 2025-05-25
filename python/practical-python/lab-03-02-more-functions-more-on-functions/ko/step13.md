# 연습 3.3: CSV 파일 읽기

시작하려면 CSV 파일을 딕셔너리 목록으로 읽는 문제에 집중해 보겠습니다. `fileparse_3.3.py` 파일에서 다음과 같은 함수를 정의하세요.

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

이 함수는 파일을 열고, `csv` 모듈로 래핑하고, 빈 줄을 무시하는 등의 세부 사항을 숨기면서 CSV 파일을 딕셔너리 목록으로 읽습니다.

시도해 보세요:

힌트: `python3 -i fileparse_3.3.py`.

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
>>>
```

이것은 좋지만, 모든 데이터가 문자열로 표현되기 때문에 데이터를 사용하여 유용한 계산을 수행할 수 없습니다. 곧 수정할 예정이지만, 계속해서 구축해 보겠습니다.
