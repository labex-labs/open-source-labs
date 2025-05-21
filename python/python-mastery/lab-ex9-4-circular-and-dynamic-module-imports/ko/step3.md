# 서브클래스 등록 구현하기

프로그래밍에서 순환 import 는 까다로운 문제일 수 있습니다. formatter 클래스를 직접 import 하는 대신, 등록 패턴을 사용할 수 있습니다. 이 패턴에서 서브클래스는 자체적으로 상위 클래스에 등록됩니다. 이는 순환 import 를 피하는 일반적이고 효과적인 방법입니다.

먼저, 클래스의 모듈 이름을 찾는 방법을 이해해 보겠습니다. 모듈 이름은 등록 패턴에서 사용할 것이므로 중요합니다. 이를 위해 터미널에서 Python 명령을 실행합니다.

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

이 명령을 실행하면 다음과 같은 출력이 표시됩니다.

```
structly.tableformat.formats.text
text
```

이 출력은 클래스 자체에서 모듈의 이름을 추출할 수 있음을 보여줍니다. 나중에 이 모듈 이름을 사용하여 서브클래스를 등록합니다.

이제 `tableformat/formatter.py` 파일에서 `TableFormatter` 클래스를 수정하여 등록 메커니즘을 추가해 보겠습니다. WebIDE 에서 이 파일을 엽니다. `TableFormatter` 클래스에 몇 가지 코드를 추가합니다. 이 코드는 서브클래스를 자동으로 등록하는 데 도움이 됩니다.

```python
class TableFormatter(ABC):
    _formats = { }  # 등록된 포맷터를 저장하는 딕셔너리

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

`__init_subclass__` 메서드는 Python 의 특수 메서드입니다. `TableFormatter`의 서브클래스가 생성될 때마다 호출됩니다. 이 메서드에서 서브클래스의 모듈 이름을 추출하여 `_formats` 딕셔너리에 서브클래스를 등록하는 키로 사용합니다.

다음으로, 등록 딕셔너리를 사용하도록 `create_formatter` 함수를 수정해야 합니다. 이 함수는 주어진 이름에 따라 적절한 formatter 를 생성하는 역할을 합니다.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
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

이러한 변경을 수행한 후 파일을 저장합니다. 그런 다음 프로그램이 여전히 작동하는지 테스트해 보겠습니다. `stock.py` 스크립트를 실행합니다.

```bash
python3 stock.py
```

프로그램이 올바르게 실행되면 변경 사항이 아무것도 손상시키지 않았다는 의미입니다. 이제 등록이 어떻게 작동하는지 확인하기 위해 `_formats` 딕셔너리의 내용을 살펴보겠습니다.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

다음과 같은 출력이 표시되어야 합니다.

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

이 출력은 서브클래스가 `_formats` 딕셔너리에 올바르게 등록되고 있음을 확인합니다. 그러나 여전히 파일 중간에 몇 가지 import 가 있습니다. 다음 단계에서는 동적 import 를 사용하여 이 문제를 해결합니다.
