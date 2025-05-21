# 컨텍스트 이해

이전 연습에서 CSV 파일을 읽고 데이터를 다양한 데이터 구조에 저장하는 코드를 접했을 수 있습니다. 이 코드의 목적은 CSV 파일에서 원시 텍스트 데이터를 가져와 딕셔너리 또는 클래스 인스턴스와 같은 더 유용한 Python 객체로 변환하는 것입니다. 이 변환은 Python 프로그램 내에서 데이터를 더 구조적이고 의미 있는 방식으로 작업할 수 있게 해주기 때문에 필수적입니다.

CSV 파일을 읽는 일반적인 패턴은 종종 특정 구조를 따릅니다. 다음은 CSV 파일을 읽고 각 행을 딕셔너리로 변환하는 함수의 예입니다.

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

이 함수가 어떻게 작동하는지 살펴보겠습니다. 먼저, Python 에서 CSV 파일 작업을 위한 기능을 제공하는 `csv` 모듈을 가져옵니다. 이 함수는 두 개의 매개변수를 사용합니다. `filename`은 읽을 CSV 파일의 이름이고, `types`는 각 열의 데이터를 적절한 데이터 유형으로 변환하는 데 사용되는 함수의 목록입니다.

함수 내부에서는 CSV 파일의 각 행을 나타내는 딕셔너리를 저장하기 위해 `records`라는 빈 목록을 초기화합니다. 그런 다음 `with` 문을 사용하여 파일을 엽니다. 이 문은 코드 블록이 실행된 후 파일이 제대로 닫히도록 보장합니다. `csv.reader` 함수는 CSV 파일의 각 행을 읽는 반복자를 생성하는 데 사용됩니다. 첫 번째 행은 헤더로 간주되므로 `next` 함수를 사용하여 검색됩니다.

다음으로, 함수는 CSV 파일의 나머지 행을 반복합니다. 각 행에 대해 딕셔너리 컴프리헨션을 사용하여 딕셔너리를 생성합니다. 딕셔너리의 키는 열 헤더이고, 값은 `types` 목록에서 해당 유형 변환 함수를 행의 값에 적용한 결과입니다. 마지막으로, 딕셔너리가 `records` 목록에 추가되고 함수는 딕셔너리 목록을 반환합니다.

이제 CSV 파일에서 클래스 인스턴스로 데이터를 읽는 유사한 함수를 살펴보겠습니다.

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

이 함수는 이전 함수와 유사하지만 딕셔너리를 생성하는 대신 클래스의 인스턴스를 생성합니다. 이 함수는 두 개의 매개변수를 사용합니다. `filename`은 읽을 CSV 파일의 이름이고, `cls`는 인스턴스가 생성될 클래스입니다.

함수 내부에서는 이전 함수와 유사한 구조를 따릅니다. 클래스 인스턴스를 저장하기 위해 `records`라는 빈 목록을 초기화합니다. 그런 다음 파일을 열고, 헤더를 읽고, 나머지 행을 반복합니다. 각 행에 대해 클래스 `cls`의 `from_row` 메서드를 호출하여 행의 데이터를 사용하여 클래스의 인스턴스를 생성합니다. 그런 다음 인스턴스가 `records` 목록에 추가되고 함수는 인스턴스 목록을 반환합니다.

이 랩에서는 이러한 함수를 리팩토링하여 더 유연하고 강력하게 만들 것입니다. 또한 함수의 매개변수와 반환 값의 예상 유형을 지정할 수 있는 Python 의 타입 힌트 (type hinting) 시스템을 탐구할 것입니다. 이를 통해 코드를 더 읽기 쉽고 이해하기 쉽게 만들 수 있으며, 특히 코드를 함께 작업할 수 있는 다른 개발자에게 유용합니다.

`reader.py` 파일을 만들고 이러한 초기 함수를 추가하는 것으로 시작해 보겠습니다. 다음 단계로 넘어가기 전에 이러한 함수가 제대로 작동하는지 확인하기 위해 테스트하십시오.
