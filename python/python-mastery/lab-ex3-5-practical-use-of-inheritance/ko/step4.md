# 추가 형식 지정자 생성

프로그래밍에서 상속은 기존 클래스를 기반으로 새로운 클래스를 만들 수 있게 해주는 강력한 개념입니다. 이는 코드 재사용을 돕고 프로그램을 더 확장 가능하게 만듭니다. 이 실험의 이 부분에서는 상속을 사용하여 CSV 및 HTML 과 같은 서로 다른 출력 형식에 대한 두 개의 새로운 형식 지정자를 만들 것입니다. 이러한 형식 지정자는 기본 클래스에서 상속받으므로 일부 공통 동작을 공유하면서 고유한 방식으로 데이터를 형식화합니다.

이제 `tableformat.py` 파일에 다음 클래스를 추가해 보겠습니다. 이러한 클래스는 각각 CSV 및 HTML 형식으로 데이터를 형식화하는 방법을 정의합니다.

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

`CSVTableFormatter` 클래스는 CSV(Comma-Separated Values, 쉼표로 구분된 값) 형식으로 데이터를 형식화하도록 설계되었습니다. `headings` 메서드는 헤더 목록을 가져와 쉼표로 구분하여 인쇄합니다. `row` 메서드는 단일 행에 대한 데이터 목록을 가져와 쉼표로 구분하여 인쇄합니다.

반면에 `HTMLTableFormatter` 클래스는 HTML 테이블 코드를 생성하는 데 사용됩니다. `headings` 메서드는 HTML `<th>` 태그를 사용하여 테이블 헤더를 만들고, `row` 메서드는 HTML `<td>` 태그를 사용하여 테이블 행을 만듭니다.

이러한 새로운 형식 지정자가 어떻게 작동하는지 테스트해 보겠습니다.

1. 먼저 CSV 형식 지정자를 테스트해 보겠습니다.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

이 코드에서는 먼저 필요한 모듈을 가져옵니다. 그런 다음 `portfolio.csv`라는 CSV 파일에서 데이터를 읽고 `Stock` 클래스의 인스턴스를 만듭니다. 다음으로, `CSVTableFormatter` 클래스의 인스턴스를 만듭니다. 마지막으로, `print_table` 함수를 사용하여 포트폴리오 데이터를 CSV 형식으로 인쇄합니다.

다음과 같은 CSV 형식의 출력이 표시됩니다.

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. 이제 HTML 형식 지정자를 테스트해 보겠습니다.

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

여기서는 `HTMLTableFormatter` 클래스의 인스턴스를 만들고 `print_table` 함수를 다시 사용하여 포트폴리오 데이터를 HTML 형식으로 인쇄합니다.

다음과 같은 HTML 형식의 출력이 표시됩니다.

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

보시다시피, 각 형식 지정자는 서로 다른 형식으로 출력을 생성하지만 모두 `TableFormatter` 기본 클래스에 의해 정의된 동일한 인터페이스를 공유합니다. 이는 상속과 다형성 (polymorphism) 의 강력함을 보여주는 훌륭한 예입니다. 기본 클래스로 작동하는 코드를 작성할 수 있으며, 이는 자동으로 모든 서브클래스에서도 작동합니다.

`print_table()` 함수는 사용 중인 특정 형식 지정자에 대해 아무것도 알 필요가 없습니다. 기본 클래스에 정의된 메서드를 호출하기만 하면 제공된 형식 지정자의 유형에 따라 적절한 구현이 선택됩니다. 이렇게 하면 코드가 더 유연해지고 유지 관리가 쉬워집니다.
