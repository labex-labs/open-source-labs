# 쉘 경험 향상시키기

쉘 경험을 향상시키려면 대화형 세션으로 가져올 수 있는 헬퍼 메서드가 있는 모듈 (`shelltools.py`) 을 생성하십시오. 이 모듈에는 데이터베이스 초기화 또는 테이블 삭제와 같은 작업에 대한 추가 헬퍼 메서드가 포함될 수 있습니다.

```python
# File: shelltools.py

def initialize_database():
    # Code to initialize the database
    pass

def drop_tables():
    # Code to drop tables
    pass
```

대화형 쉘에서 `shelltools` 모듈에서 원하는 메서드를 가져오십시오.

```python
# File: shell.py
# Execution: python shell.py

from shelltools import initialize_database, drop_tables

# Import desired methods from shelltools module
from shelltools import *

# Use imported methods
initialize_database()
drop_tables()
```
