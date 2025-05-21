# 구체적인 형식 지정자 구현

이제 추상 기본 클래스를 정의하고 `print_table()` 함수를 업데이트했으므로 구체적인 형식 지정자 클래스를 만들 차례입니다. 구체적인 형식 지정자 클래스는 추상 기본 클래스에 정의된 메서드에 대한 실제 구현을 제공하는 클래스입니다. 이 경우, 데이터를 일반 텍스트 테이블로 형식화할 수 있는 클래스를 만들 것입니다.

`tableformat.py` 파일에 다음 클래스를 추가해 보겠습니다. 이 클래스는 `TableFormatter` 추상 기본 클래스에서 상속받아 `headings()` 및 `row()` 메서드를 구현합니다.

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

`TextTableFormatter` 클래스는 `TableFormatter`에서 상속받습니다. 즉, `TableFormatter` 클래스에서 모든 속성 (property) 과 메서드를 가져오지만, `headings()` 및 `row()` 메서드에 대한 자체 구현도 제공합니다. 이러한 메서드는 각각 테이블 헤더와 행을 형식화하는 역할을 합니다. `headings()` 메서드는 헤더를 보기 좋게 형식화하여 인쇄한 다음, 헤더와 데이터를 구분하기 위해 대시 줄을 인쇄합니다. `row()` 메서드는 각 데이터 행을 유사한 방식으로 형식화합니다.

이제 새로운 형식 지정자를 테스트해 보겠습니다. `stock`, `reader`, `tableformat` 모듈을 사용하여 CSV 파일에서 데이터를 읽고 새로운 형식 지정자를 사용하여 인쇄합니다.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

이 코드를 실행하면 이전과 동일한 출력이 표시됩니다. 이는 새로운 형식 지정자가 원래의 `print_table()` 함수와 동일한 일반 텍스트 테이블을 생성하도록 설계되었기 때문입니다.

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

이 출력은 `TextTableFormatter`가 올바르게 작동하고 있음을 확인합니다. 이 접근 방식을 사용하는 장점은 코드를 더 모듈화하고 확장 가능하게 만들었다는 것입니다. 형식 지정 로직을 별도의 클래스 계층 구조로 분리함으로써 새로운 출력 형식을 쉽게 추가할 수 있습니다. `print_table()` 함수를 수정하지 않고 `TableFormatter`의 새로운 서브클래스를 만들기만 하면 됩니다. 이러한 방식으로, 향후 CSV 또는 HTML 과 같은 다양한 출력 형식을 지원할 수 있습니다.
