# 순환 import (Circular Imports) 탐구

순환 import 는 두 개 이상의 모듈이 서로 의존하는 상황입니다. 구체적으로, 모듈 A 가 모듈 B 를 import 하고, 모듈 B 도 직접 또는 간접적으로 모듈 A 를 import 하는 경우입니다. 이는 Python 의 import 시스템이 제대로 해결할 수 없는 종속성 루프를 생성합니다. 더 간단히 말하면, Python 은 어떤 모듈을 먼저 import 해야 할지 결정하기 위해 루프에 갇히게 되며, 이는 프로그램에서 오류로 이어질 수 있습니다.

순환 import 가 문제를 일으킬 수 있는 방식을 확인하기 위해 코드를 실험해 보겠습니다.

먼저, 현재 구조에서 주식 프로그램이 작동하는지 확인하기 위해 실행합니다. 이 단계는 기준선을 설정하고 변경하기 전에 프로그램이 예상대로 작동하는지 확인하는 데 도움이 됩니다.

```bash
cd ~/project/structly
python3 stock.py
```

프로그램은 올바르게 실행되어 형식화된 테이블에 주식 데이터를 표시해야 합니다. 그렇다면 현재 코드 구조는 순환 import 문제 없이 제대로 작동하고 있다는 의미입니다.

이제 `formatter.py` 파일을 수정해 보겠습니다. 일반적으로 import 를 파일 상단으로 이동하는 것이 좋습니다. 이렇게 하면 코드가 더 체계적이고 한눈에 이해하기 쉬워집니다.

```bash
cd ~/project/structly
```

WebIDE 에서 `tableformat/formatter.py`를 엽니다. 다음 import 를 기존 import 바로 뒤, 파일 상단으로 이동합니다. 이러한 import 는 텍스트, CSV 및 HTML 과 같은 다양한 테이블 포맷터에 대한 것입니다.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

따라서 파일의 시작 부분은 다음과 같아야 합니다.

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

파일을 저장하고 주식 프로그램을 다시 실행해 봅니다.

```bash
python3 stock.py
```

`TableFormatter`가 정의되지 않았다는 오류 메시지가 표시되어야 합니다. 이는 순환 import 문제의 명확한 징후입니다.

이 문제는 다음과 같은 일련의 이벤트로 인해 발생합니다.

1. `formatter.py`는 `formats/text.py`에서 `TextTableFormatter`를 import 하려고 시도합니다.
2. `formats/text.py`는 `formatter.py`에서 `TableFormatter`를 import 합니다.
3. Python 이 이러한 import 를 해결하려고 할 때, 어떤 모듈을 먼저 완전히 import 해야 할지 결정할 수 없기 때문에 루프에 갇히게 됩니다.

프로그램이 다시 작동하도록 변경 사항을 되돌려 보겠습니다. `tableformat/formatter.py`를 편집하고 import 를 원래 위치 ( `TableFormatter` 클래스 정의 뒤) 로 다시 이동합니다.

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
```

프로그램을 다시 실행하여 작동하는지 확인합니다.

```bash
python3 stock.py
```

이는 파일 중간에 import 가 있는 것이 코드 구성 측면에서 최선의 방법은 아니지만, 순환 import 문제를 피하기 위해 수행되었음을 보여줍니다. 다음 단계에서는 더 나은 솔루션을 살펴보겠습니다.
