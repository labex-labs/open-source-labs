# print_table() 에 타입 검사 추가하기

이 단계에서는 `tableformat.py` 파일의 `print_table()` 함수를 개선할 것입니다. `formatter` 매개변수가 유효한 `TableFormatter` 인스턴스인지 확인하는 검사를 추가할 것입니다. 왜 이런 검사가 필요할까요? 타입 검사는 코드의 안전망과 같습니다. 작업 중인 데이터가 올바른 타입인지 확인하여 찾기 어려운 많은 버그를 방지하는 데 도움이 됩니다.

## Python 에서 타입 검사 이해하기

타입 검사는 프로그래밍에서 매우 유용한 기술입니다. 개발 프로세스 초기에 오류를 잡아낼 수 있습니다. Python 에서는 다양한 유형의 객체를 자주 다루며, 때로는 특정 유형의 객체가 함수에 전달되기를 기대합니다. 객체가 특정 타입이거나 해당 타입의 서브클래스인지 확인하기 위해 `isinstance()` 함수를 사용할 수 있습니다. 예를 들어, 리스트를 예상하는 함수가 있는 경우 `isinstance()`를 사용하여 입력이 실제로 리스트인지 확인할 수 있습니다.

## print_table() 함수 수정하기

먼저, 코드 편집기에서 `tableformat.py` 파일을 엽니다. 파일 하단으로 스크롤하면 `print_table()` 함수를 찾을 수 있습니다. 초기 모습은 다음과 같습니다.

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

이 함수는 일부 데이터, 열 목록, 그리고 포맷터를 입력으로 받습니다. 그런 다음 포맷터를 사용하여 테이블을 인쇄합니다. 하지만 현재는 포맷터가 올바른 타입인지 확인하지 않습니다.

타입 검사를 추가하도록 수정해 보겠습니다. `isinstance()` 함수를 사용하여 `formatter` 매개변수가 `TableFormatter`의 인스턴스인지 확인합니다. 그렇지 않은 경우 명확한 메시지와 함께 `TypeError`를 발생시킵니다. 수정된 코드는 다음과 같습니다.

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## 타입 검사 구현 테스트하기

이제 타입 검사를 추가했으므로 제대로 작동하는지 확인해야 합니다. `test_tableformat.py`라는 새 Python 파일을 만들어 보겠습니다. 여기에 넣어야 할 코드는 다음과 같습니다.

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

이 코드에서는 먼저 일부 포트폴리오 데이터를 읽습니다. 그런 다음 `TableFormatter`를 상속하지 않는 `MyFormatter`라는 새 포맷터 클래스를 정의합니다. `print_table()` 함수에서 이 비호환 포맷터를 사용해 봅니다. 타입 검사가 작동하면 `TypeError`가 발생해야 합니다.

테스트를 실행하려면 터미널을 열고 `test_tableformat.py` 파일이 있는 디렉토리로 이동합니다. 그런 다음 다음 명령을 실행합니다.

```bash
python test_tableformat.py
```

모든 것이 제대로 작동하면 다음과 같은 출력이 표시됩니다.

```
Test passed - caught error: Expected a TableFormatter
```

이 출력은 타입 검사가 예상대로 작동함을 확인합니다. 이제 `print_table()` 함수는 `TableFormatter`의 인스턴스 또는 해당 서브클래스 중 하나인 포맷터만 허용합니다.
