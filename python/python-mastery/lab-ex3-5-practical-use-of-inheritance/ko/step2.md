# 기본 클래스 생성 및 인쇄 함수 수정

프로그래밍에서 상속은 클래스 계층 구조를 만들 수 있게 해주는 강력한 개념입니다. 다양한 형식으로 데이터를 출력하기 위해 상속을 사용하려면 먼저 기본 클래스를 만들어야 합니다. 기본 클래스는 다른 클래스를 위한 청사진 역할을 하며, 서브클래스가 상속하고 재정의할 수 있는 공통 메서드 집합을 정의합니다.

이제 모든 테이블 형식 지정자에 대한 인터페이스를 정의할 기본 클래스를 만들어 보겠습니다. WebIDE 에서 `tableformat.py` 파일을 열고 파일 맨 위에 다음 코드를 추가합니다.

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

`TableFormatter` 클래스는 추상 기본 클래스 (abstract base class) 입니다. 추상 기본 클래스는 메서드를 정의하지만 해당 메서드에 대한 구현을 제공하지 않는 클래스입니다. 대신, 서브클래스가 이러한 구현을 제공할 것으로 예상합니다. `NotImplementedError` 예외는 이러한 메서드가 서브클래스에 의해 재정의되어야 함을 나타내는 데 사용됩니다. 서브클래스가 이러한 메서드를 재정의하지 않고 사용하려고 하면 오류가 발생합니다.

다음으로, `print_table()` 함수를 수정하여 `TableFormatter` 클래스를 사용해야 합니다. `print_table()` 함수는 객체 목록에서 테이블 데이터를 인쇄하는 데 사용됩니다. `TableFormatter` 클래스를 사용하도록 수정하면 함수를 더 유연하게 만들고 다양한 테이블 형식으로 작업할 수 있습니다.

기존의 `print_table()` 함수를 다음 코드로 바꿉니다.

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

여기서 핵심적인 변경 사항은 `print_table()`이 이제 `formatter` 매개변수를 받는다는 것입니다. 이 매개변수는 `TableFormatter` 또는 서브클래스의 인스턴스여야 합니다. 즉, 서로 다른 테이블 형식 지정자를 `print_table()` 함수에 전달할 수 있으며, 함수는 적절한 형식 지정자를 사용하여 테이블을 인쇄합니다. 이 함수는 `headings()` 및 `row()` 메서드를 호출하여 형식 지정자 객체에 형식 지정 책임을 위임합니다.

기본 `TableFormatter` 클래스를 사용해 보면서 변경 사항을 테스트해 보겠습니다.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

이 코드를 실행하면 오류가 표시됩니다.

```
Traceback (most recent call last):
...
NotImplementedError
```

이 오류는 추상 기본 클래스를 직접 사용하려고 하지만 메서드에 대한 구현을 제공하지 않기 때문에 발생합니다. `TableFormatter` 클래스의 `headings()` 및 `row()` 메서드는 `NotImplementedError`를 발생시키므로 Python 은 이러한 메서드가 호출될 때 무엇을 해야 할지 알 수 없습니다. 다음 단계에서는 이러한 구현을 제공하는 구체적인 서브클래스를 만들 것입니다.
