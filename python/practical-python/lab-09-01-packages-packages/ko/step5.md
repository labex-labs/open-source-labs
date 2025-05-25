# 문제점: Import (Problem: Imports)

동일한 패키지 내 파일 간의 import 는 _이제 import 에 패키지 이름을 포함해야 합니다_. 구조를 기억하세요.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

수정된 import 예시.

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

모든 import 는 *절대적 (absolute)*이며, 상대적 (relative) 이지 않습니다.

```python
import fileparse    # BREAKS. fileparse not found
...
```
