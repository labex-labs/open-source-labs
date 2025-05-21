# 열 서식 지정 문제 이해하기

이 단계에서는 현재 테이블 서식 지정 구현의 한계를 살펴볼 것입니다. 또한 이 문제에 대한 몇 가지 가능한 해결책을 검토할 것입니다.

먼저, 무엇을 할 것인지 이해해 봅시다. VSCode 편집기를 열고 프로젝트 디렉토리의 `tableformat.py` 파일을 살펴보겠습니다. 이 파일은 텍스트, CSV 또는 HTML 형식과 같이 다양한 방식으로 표 형식 데이터를 서식 지정할 수 있는 코드를 포함하고 있으므로 중요합니다.

파일을 열려면 터미널에서 다음 명령을 사용합니다. `cd` 명령은 디렉토리를 프로젝트 디렉토리로 변경하고, `code` 명령은 VSCode 에서 `tableformat.py` 파일을 엽니다.

```bash
cd ~/project
touch tableformat.py
```

파일을 열면 여러 클래스가 정의되어 있는 것을 볼 수 있습니다. 이러한 클래스는 테이블 데이터를 서식 지정하는 데 서로 다른 역할을 합니다.

- `TableFormatter`: 이것은 추상 기본 클래스입니다. 테이블 제목과 행의 서식을 지정하는 데 사용되는 메서드를 가지고 있습니다. 다른 포매터 클래스의 청사진이라고 생각하십시오.
- `TextTableFormatter`: 이 클래스는 테이블을 일반 텍스트 형식으로 출력하는 데 사용됩니다.
- `CSVTableFormatter`: CSV(쉼표로 구분된 값) 형식으로 테이블 데이터를 서식 지정하는 역할을 합니다.
- `HTMLTableFormatter`: 이 클래스는 HTML 형식으로 테이블 데이터를 서식 지정합니다.

파일에는 `print_table()` 함수도 있습니다. 이 함수는 방금 언급한 포매터 클래스를 사용하여 표 형식 데이터를 표시합니다.

이제 이러한 클래스가 어떻게 작동하는지 살펴보겠습니다. `/home/labex/project` 디렉토리에서 편집기 또는 `touch` 명령을 사용하여 `step1_test1.py`라는 새 파일을 만듭니다. 다음 Python 코드를 추가합니다.

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

파일을 저장하고 터미널에서 실행합니다.

```bash
python3 step1_test1.py
```

스크립트를 실행하면 다음과 유사한 출력이 표시됩니다.

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

이제 문제를 찾아보겠습니다. `price` 열의 값이 일관되게 서식 지정되지 않은 것을 알 수 있습니다. 일부 값은 32.2 와 같이 소수점 한 자리가 있고, 다른 값은 51.23 과 같이 소수점 두 자리가 있습니다. 금융 데이터에서는 일반적으로 서식이 일관되기를 원합니다.

원하는 출력은 다음과 같습니다.

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

이 문제를 해결하는 한 가지 방법은 `print_table()` 함수가 형식 사양을 허용하도록 수정하는 것입니다. 실제로 `tableformat.py`를 수정하지 않고 어떻게 작동하는지 살펴보겠습니다. 다음 내용으로 `step1_test2.py`라는 새 파일을 만듭니다. 이 스크립트는 시연 목적으로 `print_table` 함수를 로컬에서 재정의합니다.

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

이 스크립트를 실행합니다.

```bash
python3 step1_test2.py
```

이 접근 방식은 형식을 전달하는 것을 보여주지만, `print_table`을 수정하면 함수의 인터페이스를 변경하여 기존 코드가 원래 버전을 사용하는 경우 중단될 수 있다는 단점이 있습니다.

또 다른 접근 방식은 서브클래싱 (subclassing) 하여 사용자 지정 포매터를 만드는 것입니다. `TextTableFormatter`에서 상속하고 `row()` 메서드를 재정의하는 새 클래스를 만들 수 있습니다. `step1_test3.py` 파일을 만듭니다.

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

스크립트를 실행합니다.

```bash
python3 step1_test3.py
```

이 솔루션은 서브클래싱을 시연하는 데 효과적이지만, 모든 서식 지정 변형에 대해 새 클래스를 만드는 것은 편리하지 않습니다. 또한 상속받는 기본 클래스 (여기서는 `TextTableFormatter`) 에 묶여 있습니다.

다음 단계에서는 믹스인 클래스를 사용하여 보다 우아한 솔루션을 탐색할 것입니다.
