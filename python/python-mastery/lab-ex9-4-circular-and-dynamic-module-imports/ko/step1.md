# Import 문제 이해하기

모듈 import 가 무엇인지 이해하는 것부터 시작해 보겠습니다. Python 에서 다른 파일 (모듈) 의 함수, 클래스 또는 변수를 사용하려면 `import` 문을 사용합니다. 그러나 import 를 구성하는 방식에 따라 다양한 문제가 발생할 수 있습니다.

이제 문제가 있는 모듈 구조의 예를 살펴보겠습니다. `tableformat/formatter.py`의 코드는 파일 전체에 import 가 흩어져 있습니다. 처음에는 큰 문제가 아닌 것처럼 보일 수 있지만 유지 관리 및 종속성 문제를 야기합니다.

먼저 WebIDE 파일 탐색기를 열고 `structly` 디렉토리로 이동합니다. 몇 가지 명령을 실행하여 프로젝트의 현재 구조를 이해해 보겠습니다. `cd` 명령은 현재 작업 디렉토리를 변경하는 데 사용되며, `ls -la` 명령은 숨겨진 파일을 포함하여 현재 디렉토리의 모든 파일과 디렉토리를 나열합니다.

```bash
cd ~/project/structly
ls -la
```

이렇게 하면 프로젝트 디렉토리의 파일이 표시됩니다. 이제 `cat` 명령을 사용하여 문제가 있는 파일 중 하나를 살펴보겠습니다. 이 명령은 파일의 내용을 표시합니다.

```bash
cat tableformat/formatter.py
```

다음과 유사한 코드가 표시되어야 합니다.

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

파일 중간에 import 문이 있는 것을 확인하세요. 이는 여러 가지 이유로 문제가 됩니다.

1. 코드를 읽고 유지 관리하기가 더 어려워집니다. 파일을 볼 때 파일이 의존하는 외부 모듈을 빠르게 이해할 수 있도록 모든 import 가 처음에 표시될 것으로 예상합니다.
2. 순환 import (Circular import) 문제가 발생할 수 있습니다. 순환 import 는 두 개 이상의 모듈이 서로 의존할 때 발생하며, 이로 인해 오류가 발생하고 코드가 예상치 않게 동작할 수 있습니다.
3. 파일의 모든 import 를 맨 위에 배치하는 Python 규칙을 위반합니다. 규칙을 따르면 코드를 더 읽기 쉽고 다른 개발자가 이해하기 쉽게 만들 수 있습니다.

다음 단계에서는 이러한 문제를 자세히 살펴보고 해결하는 방법을 배우겠습니다.
