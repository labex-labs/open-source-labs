# 함수 유연성 향상

현재, 우리의 함수는 파일 이름으로 지정된 파일에서만 읽도록 제한되어 있습니다. 이는 사용성을 제한합니다. 프로그래밍에서 함수가 다양한 유형의 입력을 처리할 수 있도록 더 유연하게 만드는 것이 종종 유익합니다. 이 경우, 함수가 파일 객체 또는 기타 소스와 같은 줄을 생성하는 모든 반복 가능 항목으로 작동할 수 있다면 좋을 것입니다. 이렇게 하면 압축 파일 또는 기타 데이터 스트림에서 읽는 것과 같은 더 많은 시나리오에서 이러한 함수를 사용할 수 있습니다.

이러한 유연성을 활성화하기 위해 코드를 리팩토링해 보겠습니다.

1. `reader.py` 파일을 엽니다. 몇 가지 새로운 함수를 포함하도록 수정할 것입니다. 이러한 새로운 함수를 통해 코드가 다양한 유형의 반복 가능 항목으로 작동할 수 있습니다. 추가해야 할 코드는 다음과 같습니다.

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    반복 가능 항목에서 CSV 데이터를 딕셔너리 목록으로 구문 분석

    Args:
        lines: CSV 줄을 생성하는 반복 가능 항목
        types: 각 열에 대한 유형 변환 함수 목록

    Returns:
        CSV 줄의 데이터가 있는 딕셔너리 목록
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    반복 가능 항목에서 CSV 데이터를 클래스 인스턴스 목록으로 구문 분석

    Args:
        lines: CSV 줄을 생성하는 반복 가능 항목
        cls: 인스턴스를 생성할 클래스

    Returns:
        CSV 줄의 데이터가 있는 클래스 인스턴스 목록
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    선택적 유형 변환을 사용하여 CSV 데이터를 딕셔너리 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        types: 각 열에 대한 유형 변환 함수 목록

    Returns:
        CSV 파일의 데이터가 있는 딕셔너리 목록
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    CSV 데이터를 클래스 인스턴스 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        cls: 인스턴스를 생성할 클래스

    Returns:
        CSV 파일의 데이터가 있는 클래스 인스턴스 목록
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

코드를 리팩토링한 방식을 자세히 살펴보겠습니다.

1. `csv_as_dicts()` 및 `csv_as_instances()`라는 두 개의 더 일반적인 함수를 만들었습니다. 이러한 함수는 CSV 줄을 생성하는 모든 반복 가능 항목으로 작동하도록 설계되었습니다. 즉, 파일 이름으로 지정된 파일뿐만 아니라 다양한 유형의 입력 소스를 처리할 수 있습니다.
2. 이러한 새로운 함수를 사용하도록 `read_csv_as_dicts()` 및 `read_csv_as_instances()`를 다시 구현했습니다. 이렇게 하면 파일 이름으로 파일에서 읽는 원래 기능은 여전히 사용할 수 있지만 이제 더 유연한 함수를 기반으로 구축됩니다.
3. 이 접근 방식은 기존 코드와의 이전 버전과의 호환성을 유지합니다. 즉, 이전 함수를 사용하던 모든 코드는 예상대로 계속 작동합니다. 동시에, 라이브러리는 이제 다양한 유형의 입력 소스를 처리할 수 있으므로 더 유연해집니다.

4. 이제 이러한 새로운 함수를 테스트해 보겠습니다. `test_reader_flexibility.py`라는 파일을 만들고 다음 코드를 추가합니다. 이 코드는 다양한 유형의 입력 소스를 사용하여 새로운 함수를 테스트합니다.

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. 테스트 파일을 만든 후 터미널에서 테스트 스크립트를 실행해야 합니다. 터미널을 열고 `test_reader_flexibility.py` 파일이 있는 디렉토리로 이동합니다. 그런 다음 다음 명령을 실행합니다.

```bash
python test_reader_flexibility.py
```

출력은 다음과 유사해야 합니다.

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

이 출력은 함수가 이제 다양한 유형의 입력 소스에서 작동하면서 이전 버전과의 호환성을 유지함을 확인합니다. 리팩토링된 함수는 다음에서 데이터를 처리할 수 있습니다.

- `open()`으로 연 일반 파일
- `gzip.open()`으로 연 압축 파일
- 텍스트 줄을 생성하는 다른 모든 반복 가능 객체

이렇게 하면 코드가 훨씬 더 유연해지고 다양한 시나리오에서 사용하기 쉬워집니다.
