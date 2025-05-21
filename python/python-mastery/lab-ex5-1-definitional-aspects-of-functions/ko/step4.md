# 헤더가 없는 CSV 파일 처리

데이터 처리 세계에서 모든 CSV 파일이 첫 번째 행에 헤더를 포함하는 것은 아닙니다. 헤더는 CSV 파일의 각 열에 지정된 이름으로, 각 열이 어떤 종류의 데이터를 담고 있는지 이해하는 데 도움이 됩니다. CSV 파일에 헤더가 없으면 이를 적절하게 처리할 방법이 필요합니다. 이 섹션에서는 헤더가 있는 CSV 파일과 헤더가 없는 CSV 파일을 모두 사용할 수 있도록 호출자가 헤더를 수동으로 제공할 수 있도록 함수를 수정합니다.

1. `reader.py` 파일을 열고 헤더 처리를 포함하도록 업데이트합니다.

```python
# reader.py

import csv

def csv_as_dicts(lines, types, headers=None):
    '''
    반복 가능 항목에서 CSV 데이터를 딕셔너리 목록으로 구문 분석

    Args:
        lines: CSV 줄을 생성하는 반복 가능 항목
        types: 각 열에 대한 유형 변환 함수 목록
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 줄의 데이터가 있는 딕셔너리 목록
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # 제공된 헤더가 없으면 첫 번째 행을 헤더로 사용
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, headers=None):
    '''
    반복 가능 항목에서 CSV 데이터를 클래스 인스턴스 목록으로 구문 분석

    Args:
        lines: CSV 줄을 생성하는 반복 가능 항목
        cls: 인스턴스를 생성할 클래스
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 줄의 데이터가 있는 클래스 인스턴스 목록
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # 헤더가 제공되지 않은 경우 첫 번째 행 건너뛰기
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, headers=None):
    '''
    선택적 유형 변환을 사용하여 CSV 데이터를 딕셔너리 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        types: 각 열에 대한 유형 변환 함수 목록
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 파일의 데이터가 있는 딕셔너리 목록
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename, cls, headers=None):
    '''
    CSV 데이터를 클래스 인스턴스 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        cls: 인스턴스를 생성할 클래스
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 파일의 데이터가 있는 클래스 인스턴스 목록
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

이러한 함수에 적용한 주요 변경 사항을 이해해 보겠습니다.

1. 모든 함수에 `headers` 매개변수를 추가했으며 기본값을 `None`으로 설정했습니다. 즉, 호출자가 헤더를 제공하지 않으면 함수가 기본 동작을 사용합니다.
2. `csv_as_dicts` 함수에서 `headers` 매개변수가 `None`인 경우에만 첫 번째 행을 헤더로 사용합니다. 이를 통해 헤더가 있는 파일과 헤더가 없는 파일을 자동으로 처리할 수 있습니다.
3. `csv_as_instances` 함수에서 `headers` 매개변수가 `None`인 경우에만 첫 번째 행을 건너뜁니다. 이는 자체 헤더를 제공하는 경우 파일의 첫 번째 행이 헤더가 아닌 실제 데이터이기 때문입니다.

4. 헤더가 없는 파일로 이러한 수정을 테스트해 보겠습니다. `test_headers.py`라는 파일을 만듭니다.

```python
# test_headers.py

import reader
import stock

# Define column names for the file without headers
column_names = ['name', 'shares', 'price']

# Test reading a file without headers
portfolio = reader.read_csv_as_dicts('portfolio_noheader.csv',
                                     [str, int, float],
                                     headers=column_names)
print("First item from file without headers:", portfolio[0])
print("Total items:", len(portfolio))

# Test reading the same file as instances
portfolio = reader.read_csv_as_instances('portfolio_noheader.csv',
                                        stock.Stock,
                                        headers=column_names)
print("\nFirst item as Stock instance:", portfolio[0])
print("Total items:", len(portfolio))

# Verify that original functionality still works
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item from file with headers:", portfolio[0])
```

이 테스트 스크립트에서 먼저 헤더가 없는 파일의 열 이름을 정의합니다. 그런 다음 헤더가 없는 파일을 딕셔너리 목록과 클래스 인스턴스 목록으로 읽는 것을 테스트합니다. 마지막으로 헤더가 있는 파일을 읽어 원래 기능이 여전히 작동하는지 확인합니다.

3. 터미널에서 테스트 스크립트를 실행합니다.

```bash
python test_headers.py
```

출력은 다음과 유사해야 합니다.

```
First item from file without headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7

First item from file with headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

이 출력은 이제 함수가 헤더가 있는 CSV 파일과 헤더가 없는 CSV 파일을 모두 처리할 수 있음을 확인합니다. 사용자는 필요할 때 열 이름을 제공하거나 첫 번째 행에서 헤더를 읽는 기본 동작에 의존할 수 있습니다.

이러한 수정을 통해 CSV 리더 함수는 이제 더 다양해지고 더 광범위한 파일 형식을 처리할 수 있습니다. 이는 코드를 더 강력하게 만들고 다양한 시나리오에서 유용하게 만드는 중요한 단계입니다.
