# 속성 접근을 사용하여 테이블 포맷터 만들기

프로그래밍에서 속성 접근은 객체의 속성과 상호 작용할 수 있게 해주는 기본적인 개념입니다. 이제 속성 접근에 대해 배운 내용을 실습해 보겠습니다. 유용한 유틸리티인 테이블 포맷터를 만들 것입니다. 이 포맷터는 객체 모음을 가져와 표 형식으로 표시하여 데이터를 더 쉽게 읽고 이해할 수 있도록 합니다.

## tableformat.py 모듈 만들기

먼저, 새 Python 파일을 만들어야 합니다. 이 파일에는 테이블 포맷터에 대한 코드가 포함됩니다.

파일을 만들려면 다음 단계를 따르세요.

1. WebIDE 에서 "File" 메뉴를 클릭합니다.
2. 드롭다운에서 "New File"을 선택합니다.
3. 새로 생성된 파일을 `/home/labex/project/` 디렉토리에 `tableformat.py`로 저장합니다.

이제 파일이 있으므로 `tableformat.py` 내부에 `print_table()` 함수에 대한 코드를 작성해 보겠습니다. 이 함수는 객체를 테이블 형식으로 서식 지정하고 인쇄하는 역할을 합니다.

```python
def print_table(objects, fields):
    """
    Print a collection of objects as a formatted table.

    Args:
        objects: A sequence of objects
        fields: A list of attribute names
    """
    # Print the header
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Print the separator line
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Print the data
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

이 함수가 수행하는 작업을 자세히 살펴보겠습니다.

1. 객체 시퀀스와 속성 이름 목록의 두 가지 인수를 사용합니다. 객체 시퀀스는 표시하려는 데이터이고, 속성 이름 목록은 객체의 어떤 속성을 표시할지 함수에 알려줍니다.
2. 헤더 행을 인쇄합니다. 헤더 행에는 관심 있는 속성의 이름이 포함됩니다.
3. 구분선 (separator line) 을 인쇄합니다. 이 줄은 헤더와 데이터를 시각적으로 구분하는 데 도움이 됩니다.
4. 시퀀스의 각 객체에 대해 지정된 각 속성의 값을 인쇄합니다. `getattr()` 함수를 사용하여 각 객체의 속성 값에 접근합니다.

이제 `print_table()` 함수가 예상대로 작동하는지 테스트해 보겠습니다.

```python
# Open a Python interactive shell
python3

# Import our modules
from stock import read_portfolio
import tableformat

# Read the portfolio data
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a table with name, shares, and price columns
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

위 코드를 실행하면 다음과 같은 출력이 표시됩니다.

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

`print_table()` 함수의 가장 큰 장점 중 하나는 유연성입니다. `fields` 목록을 변경하기만 하면 표시되는 열을 변경할 수 있습니다.

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

이 코드를 실행하면 다음과 같은 출력이 생성됩니다.

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

이 접근 방식의 강력함은 일반성에 있습니다. 표시하려는 속성 이름을 알고 있는 한, 동일한 `print_table()` 함수를 사용하여 모든 유형의 객체에 대한 테이블을 인쇄할 수 있습니다. 이는 테이블 포맷터를 프로그래밍 도구 상자에서 매우 유용한 도구로 만듭니다.
