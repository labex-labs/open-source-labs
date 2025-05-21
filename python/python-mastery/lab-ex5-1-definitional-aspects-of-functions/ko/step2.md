# 기본 CSV 리더 함수 생성

CSV 데이터를 읽기 위한 두 개의 기본 함수를 사용하여 `reader.py` 파일을 먼저 만들어 보겠습니다. 이러한 함수는 데이터를 딕셔너리 또는 클래스 인스턴스로 변환하는 등 다양한 방식으로 CSV 파일을 처리하는 데 도움이 됩니다.

먼저, CSV 파일이 무엇인지 이해해야 합니다. CSV 는 쉼표로 구분된 값 (Comma-Separated Values) 의 약자입니다. 각 줄이 행을 나타내고 각 행의 값이 쉼표로 구분된 테이블 형식 데이터를 저장하는 데 사용되는 간단한 파일 형식입니다.

이제 `reader.py` 파일을 만들어 보겠습니다. 다음 단계를 따르세요.

1. 코드 편집기를 열고 `/home/labex/project` 디렉토리에 `reader.py`라는 새 파일을 만듭니다. 여기에서 CSV 데이터를 읽는 함수를 작성합니다.

2. `reader.py`에 다음 코드를 추가합니다.

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    선택적 유형 변환을 사용하여 CSV 데이터를 딕셔너리 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        types: 각 열에 대한 유형 변환 함수 목록

    Returns:
        CSV 파일의 데이터가 있는 딕셔너리 목록
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    CSV 데이터를 클래스 인스턴스 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        cls: 인스턴스를 생성할 클래스

    Returns:
        CSV 파일의 데이터가 있는 클래스 인스턴스 목록
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

`read_csv_as_dicts` 함수에서 먼저 `open` 함수를 사용하여 CSV 파일을 엽니다. 그런 다음 `csv.reader`를 사용하여 파일을 줄 단위로 읽습니다. `next(rows)` 문은 일반적으로 헤더가 포함된 파일의 첫 번째 줄을 읽습니다. 그 후 나머지 행을 반복합니다. 각 행에 대해 헤더가 키이고 해당 행의 해당 값이 값인 딕셔너리를 생성합니다. 선택적으로 `types` 목록을 사용하여 유형 변환을 수행합니다.

`read_csv_as_instances` 함수는 유사하지만 딕셔너리를 생성하는 대신 주어진 클래스의 인스턴스를 생성합니다. 이 함수는 클래스에 데이터 행에서 인스턴스를 생성할 수 있는 `from_row`라는 정적 메서드가 있다고 가정합니다.

3. 이러한 함수가 제대로 작동하는지 테스트해 보겠습니다. 다음 코드를 사용하여 `test_reader.py`라는 새 파일을 만듭니다.

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

`test_reader.py` 파일에서 방금 생성한 `reader` 모듈과 `stock` 모듈을 가져옵니다. 그런 다음 `portfolio.csv`라는 샘플 CSV 파일로 두 함수를 호출하여 테스트합니다. 함수가 예상대로 작동하는지 확인하기 위해 포트폴리오의 첫 번째 항목과 총 항목 수를 출력합니다.

4. 터미널에서 테스트 스크립트를 실행합니다.

```bash
python test_reader.py
```

출력은 다음과 유사해야 합니다.

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

이는 두 함수가 올바르게 작동함을 확인합니다. 첫 번째 함수는 CSV 데이터를 적절한 유형 변환을 사용하여 딕셔너리 목록으로 변환하고, 두 번째 함수는 제공된 클래스에서 정적 메서드를 사용하여 클래스 인스턴스를 생성합니다.

다음 단계에서는 파일 이름뿐만 아니라 모든 반복 가능한 데이터 소스에서 작동하도록 허용하여 이러한 함수를 더 유연하게 리팩토링할 것입니다.
