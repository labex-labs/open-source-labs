# CSV 처리를 위한 유틸리티 함수 생성

이제 Python 의 일급 객체가 데이터 변환에 어떻게 도움이 되는지 이해했으므로, 재사용 가능한 유틸리티 함수를 만들 것입니다. 이 함수는 CSV 데이터를 읽어 딕셔너리 목록으로 변환합니다. CSV 파일은 일반적으로 표 형식 데이터를 저장하는 데 사용되며, 이를 딕셔너리 목록으로 변환하면 Python 에서 데이터를 더 쉽게 사용할 수 있으므로 매우 유용한 작업입니다.

## CSV 리더 유틸리티 생성

먼저, WebIDE 를 엽니다. 열리면 프로젝트 디렉토리로 이동하여 `reader.py`라는 새 파일을 만듭니다. 이 파일에서 CSV 데이터를 읽고 타입 변환을 적용하는 함수를 정의합니다. CSV 파일의 데이터는 일반적으로 문자열로 읽히지만, 추가 처리를 위해 정수 또는 부동 소수점 숫자와 같은 다른 데이터 타입이 필요할 수 있으므로 타입 변환이 중요합니다.

`reader.py`에 다음 코드를 추가합니다.

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dictionaries, converting each field according
    to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    list: List of dictionaries representing the CSV data
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        for row in rows:
            # Apply type conversions to each value in the row
            converted_row = [func(val) for func, val in zip(types, row)]

            # Create a dictionary mapping headers to converted values
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

이 함수는 먼저 지정된 CSV 파일을 엽니다. 그런 다음 CSV 파일의 헤더, 즉 열 이름을 읽습니다. 그 후, 파일의 각 행을 반복합니다. 행의 각 값에 대해 `types` 목록에서 해당 타입 변환 함수를 적용합니다. 마지막으로, 키가 열 헤더이고 값이 변환된 데이터인 딕셔너리를 생성하고 이 딕셔너리를 `records` 목록에 추가합니다. 모든 행이 처리되면 `records` 목록을 반환합니다.

## 유틸리티 함수 테스트

유틸리티 함수를 테스트해 보겠습니다. 먼저, 터미널을 열고 다음을 입력하여 Python 인터프리터를 시작합니다.

```bash
python3
```

이제 Python 인터프리터에 들어갔으므로, 함수를 사용하여 포트폴리오 데이터를 읽을 수 있습니다. 포트폴리오 데이터는 주식 이름, 주식 수, 가격과 같은 주식 정보를 포함하는 CSV 파일입니다.

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

이 코드를 실행하면 다음과 유사한 출력을 볼 수 있습니다.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

이 출력은 포트폴리오 데이터의 처음 세 레코드를 보여주며, 데이터 타입이 올바르게 변환되었습니다.

CTA 버스 데이터로도 함수를 사용해 보겠습니다. CTA 버스 데이터는 버스 노선, 날짜, 요일 유형 및 승차 횟수에 대한 정보를 포함하는 또 다른 CSV 파일입니다.

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

출력은 다음과 같아야 합니다.

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

이것은 함수가 다른 CSV 파일을 처리하고 적절한 타입 변환을 적용할 수 있음을 보여줍니다.

Python 인터프리터를 종료하려면 다음을 입력합니다.

```python
exit()
```

이제 모든 CSV 파일을 읽고 적절한 타입 변환을 적용할 수 있는 재사용 가능한 유틸리티 함수를 만들었습니다. 이것은 Python 의 일급 객체의 강력함과 유연하고 재사용 가능한 코드를 만드는 데 어떻게 사용할 수 있는지를 보여줍니다.
