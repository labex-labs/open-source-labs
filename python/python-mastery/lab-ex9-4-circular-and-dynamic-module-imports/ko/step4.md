# 동적 import (Dynamic Imports) 사용하기

프로그래밍에서 import 는 다른 모듈의 코드를 가져와 해당 기능을 사용할 수 있도록 하는 데 사용됩니다. 그러나 파일 중간에 import 가 있으면 코드가 약간 지저분해지고 이해하기 어려울 수 있습니다. 이 부분에서는 이 문제를 해결하기 위해 동적 import 를 사용하는 방법을 배우겠습니다. 동적 import 는 런타임에 모듈을 로드할 수 있는 강력한 기능으로, 실제로 필요할 때만 모듈을 로드한다는 의미입니다.

먼저, 현재 `TableFormatter` 클래스 뒤에 있는 import 문을 제거해야 합니다. 이러한 import 는 프로그램이 시작될 때 로드되는 정적 import 입니다. 이렇게 하려면 WebIDE 에서 `tableformat/formatter.py` 파일을 엽니다. 파일을 연 후 다음 줄을 찾아 삭제합니다.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

터미널에서 다음 명령을 실행하여 지금 프로그램을 실행하려고 하면:

```bash
python3 stock.py
```

프로그램이 실패합니다. 그 이유는 formatter 가 `_formats` 딕셔너리에 등록되지 않기 때문입니다. 알 수 없는 형식에 대한 오류 메시지가 표시됩니다. 이는 프로그램이 제대로 작동하는 데 필요한 formatter 클래스를 찾을 수 없기 때문입니다.

이 문제를 해결하기 위해 `create_formatter` 함수를 수정합니다. 목표는 필요할 때 필요한 모듈을 동적으로 import 하는 것입니다. 아래와 같이 함수를 업데이트합니다.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

이 함수에서 가장 중요한 줄은 다음과 같습니다.

```python
__import__(f'{__package__}.formats.{name}')
```

이 줄은 형식 이름을 기반으로 모듈을 동적으로 import 합니다. 모듈이 import 되면 `TableFormatter`의 서브클래스가 자동으로 자체적으로 등록됩니다. 이는 앞서 추가한 `__init_subclass__` 메서드 덕분입니다. 이 메서드는 서브클래스가 생성될 때 호출되는 특수 Python 메서드이며, 이 경우 formatter 클래스를 등록하는 데 사용됩니다.

이러한 변경을 수행한 후 파일을 저장합니다. 그런 다음 다음 명령을 사용하여 프로그램을 다시 실행합니다.

```bash
python3 stock.py
```

이제 정적 import 를 제거했음에도 불구하고 프로그램이 올바르게 작동해야 합니다. 동적 import 가 예상대로 작동하는지 확인하기 위해 `_formats` 딕셔너리를 지우고 `create_formatter` 함수를 호출합니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

다음과 유사한 출력이 표시되어야 합니다.

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

이 출력은 동적 import 가 필요할 때 모듈을 로드하고 formatter 클래스를 등록하고 있음을 확인합니다.

동적 import 및 클래스 등록을 사용하여 더 깨끗하고 유지 관리 가능한 코드 구조를 만들었습니다. 다음과 같은 이점이 있습니다.

1. 모든 import 가 이제 파일 상단에 있으며, 이는 Python 규칙을 따릅니다. 이렇게 하면 코드를 읽고 이해하기가 더 쉬워집니다.
2. 순환 import 를 제거했습니다. 순환 import 는 무한 루프 또는 디버깅하기 어려운 오류와 같은 프로그램에서 문제를 일으킬 수 있습니다.
3. 코드가 더 유연합니다. 이제 `create_formatter` 함수를 수정하지 않고도 새로운 formatter 를 추가할 수 있습니다. 이는 새로운 기능이 시간이 지남에 따라 추가될 수 있는 실제 시나리오에서 매우 유용합니다.

동적 import 및 클래스 등록을 사용하는 이 패턴은 플러그인 시스템 및 프레임워크에서 일반적으로 사용됩니다. 이러한 시스템에서 구성 요소는 사용자의 요구 사항 또는 프로그램의 요구 사항에 따라 동적으로 로드되어야 합니다.
