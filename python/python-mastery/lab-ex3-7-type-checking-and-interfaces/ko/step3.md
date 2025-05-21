# 알고리즘 템플릿 클래스 생성하기

이 단계에서는 추상 기본 클래스를 사용하여 템플릿 메서드 패턴을 구현할 것입니다. 목표는 CSV 파싱 기능에서 코드 중복을 줄이는 것입니다. 코드 중복은 코드를 유지 관리하고 업데이트하기 어렵게 만들 수 있습니다. 템플릿 메서드 패턴을 사용하면 CSV 파싱 코드에 대한 공통 구조를 만들고 서브클래스가 특정 세부 사항을 처리하도록 할 수 있습니다.

## 템플릿 메서드 패턴 이해하기

템플릿 메서드 패턴은 행동 디자인 패턴입니다. 알고리즘의 청사진과 같습니다. 메서드에서 알고리즘의 전체 구조 또는 "골격"을 정의합니다. 그러나 모든 단계를 완전히 구현하지는 않습니다. 대신, 일부 단계를 서브클래스에 위임합니다. 즉, 서브클래스는 전체 구조를 변경하지 않고 알고리즘의 특정 부분을 재정의할 수 있습니다.

이 경우, `reader.py` 파일을 살펴보면 `read_csv_as_dicts()` 및 `read_csv_as_instances()` 함수가 많은 유사한 코드를 가지고 있음을 알 수 있습니다. 이들 간의 주요 차이점은 CSV 파일의 행에서 레코드를 생성하는 방식입니다. 템플릿 메서드 패턴을 사용하면 동일한 코드를 여러 번 작성하는 것을 피할 수 있습니다.

## CSVParser 기본 클래스 추가하기

CSV 파싱을 위한 추상 기본 클래스를 추가하는 것으로 시작해 보겠습니다. `reader.py` 파일을 엽니다. import 문 바로 뒤, 파일 맨 위에 `CSVParser` 추상 기본 클래스를 추가합니다.

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

이 `CSVParser` 클래스는 CSV 파싱을 위한 템플릿 역할을 합니다. `parse` 메서드는 파일을 열고, 헤더를 가져오고, 행을 반복하는 등 CSV 파일을 읽기 위한 공통 단계를 포함합니다. 행에서 레코드를 생성하기 위한 특정 로직은 `make_record()` 메서드로 추상화됩니다. 추상 메서드이므로 `CSVParser`에서 상속받는 모든 클래스는 이 메서드를 구현해야 합니다.

## 구체적인 파서 클래스 구현하기

이제 기본 클래스가 있으므로 구체적인 파서 클래스를 생성해야 합니다. 이러한 클래스는 특정 레코드 생성 로직을 구현합니다.

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

`DictCSVParser` 클래스는 레코드를 딕셔너리로 생성하는 데 사용됩니다. 생성자에서 유형 목록을 사용합니다. `make_record` 메서드는 이러한 유형을 사용하여 행의 값을 변환하고 딕셔너리를 생성합니다.

`InstanceCSVParser` 클래스는 레코드를 클래스의 인스턴스로 생성하는 데 사용됩니다. 생성자에서 클래스를 사용합니다. `make_record` 메서드는 해당 클래스의 `from_row` 메서드를 호출하여 행에서 인스턴스를 생성합니다.

## 원래 함수 리팩토링하기

이제 이러한 새 클래스를 사용하도록 원래 `read_csv_as_dicts()` 및 `read_csv_as_instances()` 함수를 리팩토링해 보겠습니다.

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

이러한 리팩토링된 함수는 원래 함수와 동일한 인터페이스를 갖습니다. 그러나 내부적으로는 방금 생성한 새 파서 클래스를 사용합니다. 이러한 방식으로, 공통 CSV 파싱 로직을 특정 레코드 생성 로직에서 분리했습니다.

## 구현 테스트하기

리팩토링된 코드가 제대로 작동하는지 확인해 보겠습니다. `test_reader.py`라는 파일을 만들고 다음 코드를 추가합니다.

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

테스트를 실행하려면 터미널을 열고 다음 명령을 실행합니다.

```bash
python test_reader.py
```

다음과 유사한 출력이 표시됩니다.

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

이 출력이 표시되면 리팩토링된 코드가 제대로 작동하는 것입니다. 원래 함수와 파서의 직접 사용 모두 예상 결과를 생성하고 있습니다.
