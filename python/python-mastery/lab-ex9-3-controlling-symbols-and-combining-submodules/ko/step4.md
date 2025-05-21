# 더 나은 코드 구성을 위한 모듈 분할

Python 프로젝트가 커짐에 따라 단일 모듈 파일이 상당히 커지고 여러 개의 관련되지만 별개의 구성 요소를 포함하게 될 수 있습니다. 이런 경우 모듈을 하위 모듈이 있는 패키지로 분할하는 것이 좋습니다. 이 접근 방식은 코드를 더 체계적으로 만들고, 유지 관리가 더 쉬워지며, 확장성이 향상됩니다.

## 현재 구조 이해

`tableformat.py` 모듈은 큰 모듈의 좋은 예입니다. 다음과 같이 데이터를 다른 방식으로 형식화하는 여러 형식 지정자 클래스를 포함합니다.

- `TableFormatter` (base class): 다른 모든 형식 지정자 클래스의 기본 클래스입니다. 다른 클래스가 상속하고 구현할 기본 구조와 메서드를 정의합니다.
- `TextTableFormatter`: 일반 텍스트로 데이터를 형식화하는 클래스입니다.
- `CSVTableFormatter`: CSV(Comma-Separated Values) 형식으로 데이터를 형식화하는 클래스입니다.
- `HTMLTableFormatter`: HTML(Hypertext Markup Language) 형식으로 데이터를 형식화하는 클래스입니다.

이 모듈을 각 형식 지정자 유형에 대한 별도의 파일이 있는 패키지 구조로 재구성합니다. 이렇게 하면 코드가 더 모듈화되고 관리가 더 쉬워집니다.

## 1 단계: 캐시 파일 정리

코드를 재구성하기 전에 Python 캐시 파일을 정리하는 것이 좋습니다. 이러한 파일은 코드 실행 속도를 높이기 위해 Python 에서 생성되지만, 코드를 변경할 때 문제가 발생할 수 있습니다.

```bash
cd ~/project/structly
rm -rf __pycache__
```

위 명령에서 `cd ~/project/structly`는 현재 디렉토리를 프로젝트의 `structly` 디렉토리로 변경합니다. `rm -rf __pycache__`는 `__pycache__` 디렉토리와 모든 내용을 삭제합니다. `-r` 옵션은 재귀적 (recursive) 을 의미하며, 이는 `__pycache__` 디렉토리 내의 모든 파일과 하위 디렉토리를 삭제한다는 의미입니다. `-f` 옵션은 강제 (force) 를 의미하며, 확인 없이 파일을 삭제한다는 의미입니다.

## 2 단계: 새 패키지 구조 만들기

이제 패키지에 대한 새 디렉토리 구조를 만들어 보겠습니다. `tableformat`이라는 디렉토리와 그 안에 `formats`라는 하위 디렉토리를 만듭니다.

```bash
mkdir -p tableformat/formats
```

`mkdir` 명령은 디렉토리를 만드는 데 사용됩니다. `-p` 옵션은 부모 (parents) 를 의미하며, 필요한 상위 디렉토리가 없으면 모두 생성한다는 의미입니다. 따라서 `tableformat` 디렉토리가 없으면 먼저 생성된 다음 그 안에 `formats` 디렉토리가 생성됩니다.

## 3 단계: 원본 파일 이동 및 이름 바꾸기

다음으로, 원본 `tableformat.py` 파일을 새 구조로 이동하고 이름을 `formatter.py`로 바꿉니다.

```bash
mv tableformat.py tableformat/formatter.py
```

`mv` 명령은 파일을 이동하거나 이름을 바꾸는 데 사용됩니다. 이 경우 `tableformat.py` 파일을 `tableformat` 디렉토리로 이동하고 이름을 `formatter.py`로 바꿉니다.

## 4 단계: 코드를 별도 파일로 분할

이제 각 형식 지정자에 대한 파일을 만들고 관련 코드를 해당 파일로 이동해야 합니다.

### 1. 기본 형식 지정자 파일 만들기

```bash
touch tableformat/formatter.py
```

`touch` 명령은 빈 파일을 만드는 데 사용됩니다. 이 경우 `tableformat` 디렉토리에 `formatter.py`라는 파일을 만듭니다.

`TableFormatter` 기본 클래스와 `print_table` 및 `create_formatter`와 같은 일반 유틸리티 함수는 이 파일에 유지합니다. 파일은 다음과 같이 표시됩니다.

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

`__all__` 변수는 `from module import *`를 사용할 때 어떤 심볼을 임포트해야 하는지 지정하는 데 사용됩니다. 이 경우 `TableFormatter`, `print_table` 및 `create_formatter` 심볼만 임포트하도록 지정합니다.

`TableFormatter` 클래스는 다른 모든 형식 지정자 클래스의 기본 클래스입니다. `headings` 및 `row`의 두 가지 메서드를 정의하며, 이는 서브클래스에서 구현하도록 되어 있습니다.

`print_table` 함수는 객체 목록, 열 이름 목록 및 형식 지정자 객체를 가져와 데이터를 형식화된 테이블로 출력하는 유틸리티 함수입니다.

`create_formatter` 함수는 형식 이름을 인수로 받아 적절한 형식 지정자 객체를 반환하는 팩토리 함수입니다.

이러한 변경을 한 후 파일을 저장하고 종료합니다.

### 2. 텍스트 형식 지정자 만들기

```bash
touch tableformat/formats/text.py
```

이 파일에 `TextTableFormatter` 클래스만 추가합니다.

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

`__all__` 변수는 `from module import *`를 사용할 때 `TextTableFormatter` 심볼만 임포트하도록 지정합니다.

`from ..formatter import TableFormatter` 문은 상위 디렉토리의 `formatter.py` 파일에서 `TableFormatter` 클래스를 임포트합니다.

`TextTableFormatter` 클래스는 `TableFormatter` 클래스를 상속하고 `headings` 및 `row` 메서드를 구현하여 데이터를 일반 텍스트로 형식화합니다.

이러한 변경을 한 후 파일을 저장하고 종료합니다.

### 3. CSV 형식 지정자 만들기

```bash
touch tableformat/formats/csv.py
```

이 파일에 `CSVTableFormatter` 클래스만 추가합니다.

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

이전 단계와 유사하게 `__all__` 변수를 지정하고, `TableFormatter` 클래스를 임포트하고, `headings` 및 `row` 메서드를 구현하여 데이터를 CSV 형식으로 형식화합니다.

이러한 변경을 한 후 파일을 저장하고 종료합니다.

### 4. HTML 형식 지정자 만들기

```bash
touch tableformat/formats/html.py
```

이 파일에 `HTMLTableFormatter` 클래스만 추가합니다.

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

다시, `__all__` 변수를 지정하고, `TableFormatter` 클래스를 임포트하고, `headings` 및 `row` 메서드를 구현하여 데이터를 HTML 형식으로 형식화합니다.

이러한 변경을 한 후 파일을 저장하고 종료합니다.

## 5 단계: 패키지 초기화 파일 만들기

Python 에서 `__init__.py` 파일은 디렉토리를 Python 패키지로 표시하는 데 사용됩니다. `tableformat` 및 `formats` 디렉토리 모두에 `__init__.py` 파일을 만들어야 합니다.

### 1. `tableformat` 패키지에 대한 파일 만들기

```bash
touch tableformat/__init__.py
```

파일에 이 내용을 추가합니다.

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

이 문은 `formatter.py` 파일의 모든 심볼을 임포트하고 `tableformat` 패키지를 임포트할 때 사용할 수 있도록 합니다.

이러한 변경을 한 후 파일을 저장하고 종료합니다.

### 2. `formats` 패키지에 대한 파일 만들기

```bash
touch tableformat/formats/__init__.py
```

이 파일은 비워두거나 간단한 docstring 을 추가할 수 있습니다.

```python
'''
Format implementations for different output formats.
'''
```

docstring 은 `formats` 패키지가 수행하는 작업에 대한 간략한 설명을 제공합니다.

이러한 변경을 한 후 파일을 저장하고 종료합니다.

## 6 단계: 새 구조 테스트

변경 사항이 제대로 작동하는지 확인하기 위해 간단한 테스트를 만들어 보겠습니다.

```bash
cd ~/project
touch test_tableformat.py
```

`test_tableformat.py` 파일에 이 내용을 추가합니다.

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

이 테스트 코드는 `structly` 패키지에서 필요한 함수와 클래스를 임포트하고, 각 유형의 형식 지정자를 만들고, 일부 테스트 데이터를 정의한 다음, 해당 형식으로 데이터를 출력하여 각 형식 지정자를 테스트합니다.

이러한 변경을 한 후 파일을 저장하고 종료합니다. 이제 테스트를 실행합니다.

```bash
python test_tableformat.py
```

세 가지 다른 방식 (텍스트, CSV 및 HTML) 으로 형식화된 동일한 데이터가 표시되어야 합니다. 예상 출력이 표시되면 코드 재구성이 성공한 것입니다.
