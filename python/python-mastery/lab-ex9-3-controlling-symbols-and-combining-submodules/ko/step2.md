# `__all__`을 사용하여 내보낼 심볼 제어

Python 에서 `from module import *` 문을 사용할 때 모듈에서 어떤 심볼 (함수, 클래스, 변수) 을 임포트할지 제어하고 싶을 수 있습니다. 이럴 때 `__all__` 변수가 유용합니다. `from module import *` 문은 모듈의 모든 심볼을 현재 네임스페이스로 임포트하는 방법입니다. 그러나 때로는 모든 심볼을 임포트하고 싶지 않을 수 있습니다. 특히 심볼이 많거나 일부 심볼이 모듈 내부에만 사용되도록 의도된 경우입니다. `__all__` 변수를 사용하면 이 문을 사용할 때 정확히 어떤 심볼을 임포트해야 하는지 지정할 수 있습니다.

## `__all__`이란 무엇인가?

`__all__` 변수는 문자열의 리스트입니다. 이 리스트의 각 문자열은 `from module import *` 문을 사용할 때 모듈이 내보내는 심볼 (함수, 클래스 또는 변수) 을 나타냅니다. 모듈에 `__all__` 변수가 정의되어 있지 않으면 `import *` 문은 밑줄로 시작하지 않는 모든 심볼을 임포트합니다. 밑줄로 시작하는 심볼은 일반적으로 모듈에 대한 private 또는 internal 로 간주되며 직접 임포트하도록 되어 있지 않습니다.

## 각 하위 모듈 수정

이제 `structly` 패키지의 각 하위 모듈에 `__all__` 변수를 추가해 보겠습니다. 이렇게 하면 `from module import *` 문을 사용할 때 각 하위 모듈에서 어떤 심볼이 내보내지는지 제어하는 데 도움이 됩니다.

1. 먼저, `structure.py`를 수정해 보겠습니다.

```bash
touch ~/project/structly/structure.py
```

이 명령은 프로젝트의 `structly` 디렉토리에 `structure.py`라는 새 파일을 만듭니다. 파일을 만든 후 `__all__` 변수를 추가해야 합니다. 파일 맨 위, 임포트 문 바로 뒤에 이 줄을 추가합니다.

```python
__all__ = ['Structure']
```

이 줄은 누군가 `from structure import *`를 사용할 때 `Structure` 심볼만 임포트하도록 Python 에 지시합니다. 파일을 저장하고 편집기를 종료합니다.

2. 다음으로, `reader.py`를 수정해 보겠습니다.

```bash
touch ~/project/structly/reader.py
```

이 명령은 `structly` 디렉토리에 `reader.py`라는 새 파일을 만듭니다. 이제 파일에서 `read_csv_as_`로 시작하는 모든 함수를 찾습니다. 이러한 함수가 내보내려는 함수입니다. 그런 다음 이러한 모든 함수 이름을 사용하여 `__all__` 리스트를 추가합니다. 다음과 같이 표시됩니다.

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

실제 함수 이름은 파일에서 찾은 내용에 따라 다를 수 있습니다. 찾은 모든 `read_csv_as_*` 함수를 포함해야 합니다. 파일을 저장하고 편집기를 종료합니다.

3. 이제 `tableformat.py`를 수정해 보겠습니다.

```bash
touch ~/project/structly/tableformat.py
```

이 명령은 `structly` 디렉토리에 `tableformat.py`라는 새 파일을 만듭니다. 파일 맨 위에 이 줄을 추가합니다.

```python
__all__ = ['create_formatter', 'print_table']
```

이 줄은 누군가 `from tableformat import *`를 사용할 때 `create_formatter` 및 `print_table` 심볼만 임포트하도록 지정합니다. 파일을 저장하고 편집기를 종료합니다.

## `__init__.py`에서 통합 임포트

이제 각 모듈이 내보내는 내용을 정의했으므로 `__init__.py` 파일을 업데이트하여 이러한 모든 심볼을 임포트할 수 있습니다. `__init__.py` 파일은 Python 패키지에서 특별한 파일입니다. 패키지가 임포트될 때 실행되며, 패키지를 초기화하고 하위 모듈에서 심볼을 임포트하는 데 사용할 수 있습니다.

```bash
touch ~/project/structly/__init__.py
```

이 명령은 `structly` 디렉토리에 새 `__init__.py` 파일을 만듭니다. 파일의 내용을 다음과 같이 변경합니다.

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

이러한 줄은 `structure`, `reader` 및 `tableformat` 하위 모듈에서 내보낸 모든 심볼을 임포트합니다. 모듈 이름 앞의 점 (`.`) 은 상대 임포트임을 나타냅니다. 즉, 동일한 패키지 내에서 임포트한다는 의미입니다. 파일을 저장하고 편집기를 종료합니다.

## 변경 사항 테스트

변경 사항이 제대로 작동하는지 확인하기 위해 간단한 테스트 파일을 만들어 보겠습니다. 이 테스트 파일은 `__all__` 변수에 지정한 심볼을 임포트하려고 시도하고 임포트가 성공하면 성공 메시지를 출력합니다.

```bash
touch ~/project/test_structly.py
```

이 명령은 프로젝트 디렉토리에 `test_structly.py`라는 새 파일을 만듭니다. 파일에 이 내용을 추가합니다.

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

이러한 줄은 `Structure` 클래스, `read_csv_as_instances` 함수, `create_formatter` 및 `print_table` 함수를 `structly` 패키지에서 임포트하려고 시도합니다. 임포트가 성공하면 프로그램은 "Successfully imported all required symbols!" 메시지를 출력합니다. 파일을 저장하고 편집기를 종료합니다. 이제 이 테스트를 실행해 보겠습니다.

```bash
cd ~/project
python test_structly.py
```

`cd ~/project` 명령은 현재 작업 디렉토리를 프로젝트 디렉토리로 변경합니다. `python test_structly.py` 명령은 `test_structly.py` 스크립트를 실행합니다. 모든 것이 제대로 작동하면 화면에 "Successfully imported all required symbols!" 메시지가 표시됩니다.
