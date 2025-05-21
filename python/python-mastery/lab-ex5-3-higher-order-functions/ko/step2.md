# 고차 함수 만들기

Python 에서 고차 함수는 다른 함수를 인수로 받을 수 있는 함수입니다. 이를 통해 더 큰 유연성과 코드 재사용이 가능합니다. 이제 `convert_csv()`라는 고차 함수를 만들어 보겠습니다. 이 함수는 CSV 데이터를 처리하는 일반적인 작업을 처리하는 동시에 CSV 의 각 행을 레코드로 변환하는 방식을 사용자 정의할 수 있도록 합니다.

WebIDE 에서 `reader.py` 파일을 엽니다. CSV 데이터의 반복 가능한 객체, 변환 함수, 그리고 선택적으로 열 헤더를 사용할 함수를 추가할 것입니다. 변환 함수는 CSV 의 각 행을 레코드로 변환하는 데 사용됩니다.

다음은 `convert_csv()` 함수의 코드입니다. `reader.py` 파일에 복사하여 붙여넣으세요.

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

이 함수가 하는 일을 자세히 살펴보겠습니다. 먼저, 변환된 레코드를 저장하기 위해 `records`라는 빈 리스트를 초기화합니다. 그런 다음 `csv.reader()` 함수를 사용하여 CSV 데이터의 행을 읽습니다. 헤더가 제공되지 않으면 첫 번째 행을 헤더로 사용합니다. 각 후속 행에 대해 `conversion_func`을 적용하여 행을 레코드로 변환하고 `records` 리스트에 추가합니다. 마지막으로, 레코드 목록을 반환합니다.

이제 `convert_csv()` 함수를 테스트하기 위한 간단한 변환 함수가 필요합니다. 이 함수는 헤더와 행을 받아 헤더를 키로 사용하여 행을 딕셔너리로 변환합니다.

다음은 `make_dict()` 함수의 코드입니다. 이 함수도 `reader.py` 파일에 추가하세요.

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

`make_dict()` 함수는 `zip()` 함수를 사용하여 각 헤더를 행의 해당 값과 쌍으로 연결한 다음 이러한 쌍에서 딕셔너리를 생성합니다.

이 함수들을 테스트해 보겠습니다. 터미널에서 다음 명령을 실행하여 Python 셸을 엽니다.

```bash
cd ~/project
python3 -i reader.py
```

`python3` 명령의 `-i` 옵션은 대화형 모드에서 Python 인터프리터를 시작하고 `reader.py` 파일을 가져오므로 방금 정의한 함수를 사용할 수 있습니다.

Python 셸에서 다음 코드를 실행하여 함수를 테스트합니다.

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

이 코드는 `portfolio.csv` 파일을 열고, `make_dict()` 변환 함수와 함께 `convert_csv()` 함수를 사용하여 CSV 데이터를 딕셔너리 목록으로 변환한 다음 결과를 출력합니다.

다음과 유사한 출력이 표시되어야 합니다.

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

이 출력은 고차 함수 `convert_csv()`가 올바르게 작동함을 보여줍니다. 다른 함수를 인수로 사용하는 함수를 성공적으로 만들었으며, 이를 통해 CSV 데이터의 변환 방식을 쉽게 변경할 수 있습니다.

Python 셸을 종료하려면 `exit()`를 입력하거나 Ctrl+D 를 누르세요.
