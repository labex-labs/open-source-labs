# 패키지에서 모든 항목 내보내기

Python 에서 패키지 구성은 코드를 효과적으로 관리하는 데 매우 중요합니다. 이제 패키지 구성을 한 단계 더 발전시키겠습니다. 패키지 수준에서 어떤 심볼을 내보낼지 정의할 것입니다. 심볼을 내보낸다는 것은 특정 함수, 클래스 또는 변수를 코드의 다른 부분이나 패키지를 사용할 수 있는 다른 개발자가 사용할 수 있도록 하는 것을 의미합니다.

## 패키지에 `__all__` 추가

Python 패키지로 작업할 때 누군가 `from structly import *` 문을 사용할 때 어떤 심볼에 액세스할 수 있는지 제어하고 싶을 수 있습니다. 이럴 때 `__all__` 리스트가 유용합니다. 패키지의 `__init__.py` 파일에 `__all__` 리스트를 추가하면 누군가 `from structly import *` 문을 사용할 때 정확히 어떤 심볼을 사용할 수 있는지 제어할 수 있습니다.

먼저, `__init__.py` 파일을 만들거나 업데이트해 보겠습니다. 파일이 없으면 `touch` 명령을 사용하여 파일을 만듭니다.

```bash
touch ~/project/structly/__init__.py
```

이제 `__init__.py` 파일을 열고 `__all__` 리스트를 추가합니다. 이 리스트에는 내보내려는 모든 심볼이 포함되어야 합니다. 심볼은 `structure`, `reader`, `tableformat` 모듈과 같이 출처에 따라 그룹화됩니다.

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

코드를 추가한 후 파일을 저장하고 편집기를 종료합니다.

## `import *` 이해

`from module import *` 패턴은 대부분의 Python 코드에서 일반적으로 권장되지 않습니다. 다음과 같은 몇 가지 이유가 있습니다.

1. 예상치 못한 심볼로 네임스페이스를 오염시킬 수 있습니다. 즉, 현재 네임스페이스에 예상하지 못한 변수나 함수가 있을 수 있으며, 이는 이름 충돌로 이어질 수 있습니다.
2. 특정 심볼의 출처를 알 수 없게 만듭니다. `import *`를 사용하면 심볼이 어떤 모듈에서 오는지 알기 어려워 코드를 이해하고 유지 관리하기 어려울 수 있습니다.
3. 섀도잉 (shadowing) 문제가 발생할 수 있습니다. 섀도잉은 로컬 변수 또는 함수가 다른 모듈의 변수 또는 함수와 동일한 이름을 가질 때 발생하며, 이는 예상치 못한 동작을 유발할 수 있습니다.

그러나 `import *`를 사용하는 것이 적절한 특정 경우가 있습니다.

- 전체적으로 사용하도록 설계된 패키지의 경우. 패키지가 단일 단위로 사용되도록 되어 있는 경우 `import *`를 사용하면 필요한 모든 심볼에 더 쉽게 액세스할 수 있습니다.
- 패키지가 `__all__`을 통해 명확한 인터페이스를 정의하는 경우. `__all__` 리스트를 사용하면 내보낼 심볼을 제어하여 `import *`를 더 안전하게 사용할 수 있습니다.
- Python REPL(Read-Eval-Print Loop) 과 같은 대화형 사용의 경우. 대화형 환경에서는 모든 심볼을 한 번에 임포트하는 것이 편리할 수 있습니다.

## Import \*로 테스트

모든 심볼을 한 번에 임포트할 수 있는지 확인하기 위해 다른 테스트 파일을 만들어 보겠습니다. `touch` 명령을 사용하여 파일을 만듭니다.

```bash
touch ~/project/test_import_all.py
```

이제 `test_import_all.py` 파일을 열고 다음 내용을 추가합니다. 이 코드는 `structly` 패키지의 모든 심볼을 임포트한 다음 일부 중요한 심볼을 사용할 수 있는지 테스트합니다.

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

파일을 저장하고 편집기를 종료합니다. 이제 테스트를 실행해 보겠습니다. 먼저 `cd` 명령을 사용하여 프로젝트 디렉토리로 이동한 다음 Python 스크립트를 실행합니다.

```bash
cd ~/project
python test_import_all.py
```

모든 것이 올바르게 설정되어 있으면 모든 심볼이 성공적으로 임포트되었음을 확인할 수 있습니다.
