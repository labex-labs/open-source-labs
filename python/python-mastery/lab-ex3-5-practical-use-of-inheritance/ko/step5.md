# 팩토리 함수 생성

상속을 사용할 때 흔히 발생하는 문제 중 하나는 사용자가 특정 형식 지정자 클래스의 이름을 기억해야 한다는 것입니다. 특히 클래스 수가 증가함에 따라 이는 상당히 번거로울 수 있습니다. 이 프로세스를 단순화하기 위해 팩토리 함수를 만들 수 있습니다. 팩토리 함수는 객체를 생성하고 반환하는 특수한 유형의 함수입니다. 이 경우, 간단한 형식 이름을 기반으로 적절한 형식 지정자를 반환합니다.

`tableformat.py` 파일에 다음 함수를 추가해 보겠습니다. 이 함수는 형식 이름을 인수로 받아 해당 형식 지정자 객체를 반환합니다.

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

`create_formatter()` 함수는 팩토리 함수입니다. 제공한 `format_name` 인수를 확인합니다. 'text'인 경우 `TextTableFormatter` 객체를 생성하여 반환합니다. 'csv'인 경우 `CSVTableFormatter` 객체를 반환하고, 'html'인 경우 `HTMLTableFormatter` 객체를 반환합니다. 형식 이름이 인식되지 않으면 `ValueError`를 발생시킵니다. 이러한 방식으로 사용자는 특정 클래스 이름을 알 필요 없이 간단한 이름만 제공하여 형식 지정자를 쉽게 선택할 수 있습니다.

이제 팩토리 함수를 테스트해 보겠습니다. CSV 파일에서 데이터를 읽고 다양한 형식으로 인쇄하기 위해 기존 함수와 클래스를 사용합니다.

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

이 코드에서는 먼저 필요한 모듈과 함수를 가져옵니다. 그런 다음 `portfolio.csv` 파일에서 데이터를 읽고 `portfolio` 객체를 만듭니다. 그 후, 'text', 'csv', 'html'과 같은 다양한 형식 이름으로 `create_formatter()` 함수를 테스트합니다. 각 형식에 대해 형식 지정자 객체를 만들고 형식 이름을 인쇄한 다음, `print_table()` 함수를 사용하여 지정된 형식으로 `portfolio` 데이터를 인쇄합니다.

이 코드를 실행하면 형식 이름으로 구분된 세 가지 형식의 출력이 표시됩니다.

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

팩토리 함수는 클래스 인스턴스화의 세부 정보를 숨기기 때문에 코드를 더 사용자 친화적으로 만듭니다. 사용자는 형식 지정자 객체를 만드는 방법을 알 필요가 없으며 원하는 형식을 지정하기만 하면 됩니다.

객체를 생성하기 위해 팩토리 함수를 사용하는 이 패턴은 객체 지향 프로그래밍에서 흔히 사용되는 디자인 패턴으로, 팩토리 패턴 (Factory Pattern) 이라고 합니다. 이는 클라이언트 코드 (형식 지정자를 사용하는 코드) 와 실제 구현 클래스 (형식 지정자 클래스) 사이에 추상화 계층을 제공합니다. 이렇게 하면 코드가 더 모듈화되고 사용하기 쉬워집니다.

**핵심 개념 검토:**

1.  **추상 기본 클래스 (Abstract Base Class)**: `TableFormatter` 클래스는 인터페이스 역할을 합니다. 인터페이스는 이를 구현하는 모든 클래스가 가져야 하는 메서드 집합을 정의합니다. 이 경우, 모든 형식 지정자 클래스는 `TableFormatter` 클래스에 정의된 메서드를 구현해야 합니다.

2.  **상속 (Inheritance)**: `TextTableFormatter`, `CSVTableFormatter`, `HTMLTableFormatter`와 같은 구체적인 형식 지정자 클래스는 기본 `TableFormatter` 클래스에서 상속받습니다. 즉, 기본 클래스에서 기본 구조와 메서드를 가져오고 자체적인 특정 구현을 제공할 수 있습니다.

3.  **다형성 (Polymorphism)**: `print_table()` 함수는 필요한 인터페이스를 구현하는 모든 형식 지정자와 함께 작동할 수 있습니다. 즉, `print_table()` 함수에 서로 다른 형식 지정자 객체를 전달할 수 있으며 각 객체에 대해 올바르게 작동합니다.

4.  **팩토리 패턴 (Factory Pattern)**: `create_formatter()` 함수는 형식 지정자 객체 생성을 단순화합니다. 형식 이름에 따라 올바른 객체를 생성하는 세부 사항을 처리하므로 사용자는 이에 대해 걱정할 필요가 없습니다.

이러한 객체 지향 원칙을 사용하여 다양한 출력 형식으로 표 형식 데이터를 형식화하기 위한 유연하고 확장 가능한 시스템을 만들었습니다.
