# 상대 import (Relative Imports)

패키지 이름을 직접 사용하는 대신, `.`을 사용하여 현재 패키지를 참조할 수 있습니다.

```python
from . import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

구문:

```python
from . import modname
```

이렇게 하면 패키지 이름을 쉽게 변경할 수 있습니다.
