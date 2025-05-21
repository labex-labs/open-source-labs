# 믹스인을 위한 사용자 친화적인 API 생성

믹스인은 강력하지만, 다중 상속을 직접 사용하는 것은 복잡하게 느껴질 수 있습니다. 이 단계에서는 `create_formatter()` 함수를 개선하여 이러한 복잡성을 숨기고 사용자에게 더 쉬운 API 를 제공할 것입니다.

먼저, `tableformat.py`가 편집기에서 열려 있는지 확인합니다.

```bash
cd ~/project
touch tableformat.py
```

기존 `create_formatter()` 함수를 찾습니다.

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

_전체 기존_ `create_formatter()` 함수 정의를 아래의 향상된 버전으로 바꿉니다. 이 새 버전은 열 형식 및 대문자 헤더에 대한 선택적 인수를 허용합니다.

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_자체 수정: 다중 if/elif 분기 대신 상속을 위해 동적으로 클래스 튜플을 생성합니다._

이 향상된 함수는 먼저 기본 포매터 클래스 (`TextTableFormatter`, `CSVTableFormatter` 등) 를 결정합니다. 그런 다음 선택적 인수 `column_formats` 및 `upper_headers`를 기반으로 필요한 믹스인과 기본 포매터 클래스에서 상속되는 새 클래스 (`CustomFormatter`) 를 동적으로 구성합니다. 마지막으로 이 사용자 지정 포매터의 인스턴스를 반환합니다.

**`tableformat.py`에 대한 변경 사항을 저장하는 것을 잊지 마세요.**

이제 향상된 함수를 테스트해 보겠습니다. **`tableformat.py`에 업데이트된 `create_formatter` 함수를 저장했는지 확인하십시오.**

먼저, 열 서식을 테스트합니다. `step3_test1.py`를 만듭니다.

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

스크립트를 실행합니다.

```bash
python3 step3_test1.py
```

서식이 지정된 열이 있는 테이블이 표시되어야 합니다 (다시, 가격 형식의 유형 처리에 따라 다름).

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

다음으로, 대문자 헤더를 테스트합니다. `step3_test2.py`를 만듭니다.

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

스크립트를 실행합니다.

```bash
python3 step3_test2.py
```

대문자 헤더가 있는 테이블이 표시되어야 합니다.

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

마지막으로, 두 옵션을 모두 결합합니다. `step3_test3.py`를 만듭니다.

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

스크립트를 실행합니다.

```bash
python3 step3_test3.py
```

그러면 서식이 지정된 열과 대문자 헤더가 모두 있는 테이블이 표시됩니다.

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
------------------------------------------------------------------
```

향상된 함수는 다른 포매터 유형에서도 작동합니다. 예를 들어 CSV 포매터로 사용해 보십시오. `step3_test4.py`를 만듭니다.

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

스크립트를 실행합니다.

```bash
python3 step3_test4.py
```

그러면 CSV 형식으로 대문자 헤더와 서식이 지정된 열이 생성됩니다 (다시, `print_table`에서 전달된 문자열에 대한 `%d`/`%.2f` 형식 지정의 잠재적 유형 문제).

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

`create_formatter()` 함수를 개선함으로써 사용자 친화적인 API 를 만들었습니다. 이제 사용자는 다중 상속 구조를 직접 관리할 필요 없이 믹스인 기능을 쉽게 적용할 수 있습니다.
