# Import 문 수정하기

이제 왜 이렇게 해야 하는지 이해해 봅시다. 파일을 `structly` 패키지로 옮기면서 Python 이 모듈을 찾는 방식이 변경되었습니다. 각 파일의 import 문은 새로운 패키지 구조에 맞게 업데이트해야 합니다. Python 은 이러한 import 문을 사용하여 다른 모듈의 코드를 찾고 사용하기 때문에 이는 매우 중요합니다.

`structure.py` 파일은 업데이트하는 데 매우 중요합니다. 이 파일은 `validate.py` 파일에서 함수와 클래스를 import 합니다. 이 두 파일 모두 이제 동일한 `structly` 패키지에 있으므로 import 문을 그에 맞게 조정해야 합니다.

먼저 편집기에서 `structly/structure.py` 파일을 열어 봅시다. 파일 탐색기에서 `structly/structure.py`를 클릭하거나 터미널에서 다음 명령을 실행할 수 있습니다.

```bash
# 파일 탐색기에서 structly/structure.py를 클릭하거나 다음을 실행합니다:
code structly/structure.py
```

파일이 열리면 import 문의 첫 번째 줄을 살펴봅니다. 현재 다음과 같이 표시됩니다.

```python
from validate import validate_type
```

이 문은 파일들이 다른 구조에 있을 때 올바르게 작동했습니다. 하지만 이제 Python 에게 현재 모듈과 같은 패키지 내에서 `validate` 모듈을 찾도록 알려주기 위해 변경해야 합니다. 따라서 다음과 같이 변경합니다.

```python
from .validate import validate_type
```

여기서 `validate` 앞의 점 (`.`) 이 핵심입니다. 이는 Python 에서 상대 import(relative import) 라고 하는 특별한 구문입니다. 이는 Python 에게 현재 모듈 (이 경우 `structure.py`) 과 같은 패키지 내에서 `validate` 모듈을 검색하도록 지시합니다.

이 변경을 한 후에는 파일을 저장해야 합니다. 저장은 변경 사항을 영구적으로 만들기 때문에 중요하며, 코드를 실행할 때 Python 은 업데이트된 import 문을 사용합니다.

이제 다른 파일들을 확인하여 업데이트가 필요한지 살펴봅시다.

1. `structly/reader.py` - 이 파일은 사용자 정의 모듈에서 아무것도 import 하지 않습니다. 즉, 이 파일에는 아무런 변경도 필요하지 않습니다.
2. `structly/tableformat.py` - `reader.py` 파일과 마찬가지로 이 파일도 사용자 정의 모듈에서 아무것도 import 하지 않습니다. 따라서 여기에서도 변경이 필요하지 않습니다.
3. `structly/validate.py` - 이전 두 파일과 마찬가지로 사용자 정의 모듈에서 아무것도 import 하지 않습니다. 따라서 수정할 필요가 없습니다.

실제 프로그래밍에서는 프로젝트 간에 모듈 간의 더 복잡한 관계가 있을 수 있습니다. 패키지 구조를 만들거나 수정하기 위해 파일을 이동할 때 항상 import 문을 업데이트하는 것을 기억하십시오. 이렇게 하면 코드가 필요한 모듈을 올바르게 찾고 사용할 수 있습니다.
