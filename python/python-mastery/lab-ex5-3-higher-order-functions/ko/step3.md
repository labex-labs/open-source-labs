# 기존 함수 리팩터링

이제 `convert_csv()`라는 고차 함수를 만들었습니다. 고차 함수는 다른 함수를 인수로 받거나 함수를 결과로 반환할 수 있는 함수입니다. 이는 Python 에서 더 모듈화되고 재사용 가능한 코드를 작성하는 데 도움이 되는 강력한 개념입니다. 이 섹션에서는 이 고차 함수를 사용하여 원래 함수인 `csv_as_dicts()`와 `csv_as_instances()`를 리팩터링합니다. 리팩터링은 외부 동작을 변경하지 않고 기존 코드를 재구성하여 코드 중복 제거와 같은 내부 구조를 개선하는 프로세스입니다.

WebIDE 에서 `reader.py` 파일을 열어 시작해 보겠습니다. 다음과 같이 함수를 업데이트합니다.

1. 먼저, `csv_as_dicts()` 함수를 대체합니다. 이 함수는 CSV 데이터의 행을 딕셔너리 목록으로 변환하는 데 사용됩니다. 다음은 새로운 코드입니다.

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

이 코드에서 `headers`와 `row`를 인수로 사용하는 내부 함수 `dict_converter`를 정의합니다. 딕셔너리 컴프리헨션 (dictionary comprehension) 을 사용하여 키가 헤더 이름이고 값이 해당 유형 변환 함수를 행의 값에 적용한 결과인 딕셔너리를 만듭니다. 그런 다음 `dict_converter` 함수를 인수로 사용하여 `convert_csv()` 함수를 호출합니다.

2. 다음으로, `csv_as_instances()` 함수를 대체합니다. 이 함수는 CSV 데이터의 행을 주어진 클래스의 인스턴스 목록으로 변환하는 데 사용됩니다. 다음은 새로운 코드입니다.

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

이 코드에서 `headers`와 `row`를 인수로 사용하는 내부 함수 `instance_converter`를 정의합니다. 주어진 클래스 `cls`의 `from_row` 클래스 메서드를 호출하여 행에서 인스턴스를 생성합니다. 그런 다음 `instance_converter` 함수를 인수로 사용하여 `convert_csv()` 함수를 호출합니다.

이러한 함수를 리팩터링한 후에는 예상대로 작동하는지 확인하기 위해 테스트해야 합니다. 이를 위해 Python 셸에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -i reader.py
```

`cd ~/project` 명령은 현재 작업 디렉토리를 `project` 디렉토리로 변경합니다. `python3 -i reader.py` 명령은 `reader.py` 파일을 대화형 모드로 실행합니다. 즉, 파일 실행이 완료된 후에도 Python 코드를 계속 실행할 수 있습니다.

Python 셸이 열리면 다음 코드를 실행하여 리팩터링된 함수를 테스트합니다.

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

이 코드에서는 먼저 테스트를 위해 간단한 `Stock` 클래스를 정의합니다. `__init__` 메서드는 `Stock` 인스턴스의 속성을 초기화합니다. `from_row` 클래스 메서드는 CSV 데이터의 행에서 `Stock` 인스턴스를 생성합니다. `__repr__` 메서드는 `Stock` 인스턴스의 문자열 표현을 제공합니다.

그런 다음 `portfolio.csv` 파일을 열고 유형 변환 함수 목록과 함께 함수에 전달하여 `csv_as_dicts()` 함수를 테스트합니다. 결과 목록의 첫 번째 딕셔너리를 출력합니다.

마지막으로, `portfolio.csv` 파일을 열고 `Stock` 클래스와 함께 함수에 전달하여 `csv_as_instances()` 함수를 테스트합니다. 결과 목록의 첫 번째 인스턴스를 출력합니다.

모든 것이 제대로 작동하면 다음과 유사한 출력이 표시되어야 합니다.

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

이 출력은 리팩터링된 함수가 올바르게 작동함을 나타냅니다. 동일한 기능을 유지하면서 코드 중복을 성공적으로 제거했습니다.

Python 셸을 종료하려면 `exit()`를 입력하거나 Ctrl+D 를 누르세요.
