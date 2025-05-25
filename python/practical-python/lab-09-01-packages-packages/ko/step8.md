# `__init__.py` 파일

이 파일들의 주요 목적은 모듈을 함께 묶는 것입니다.

예시: 함수 통합

```python
# porty/__init__.py
from .pcost import portfolio_cost
from .report import portfolio_report
```

이렇게 하면 import 시 이름이 *최상위 레벨*에 나타납니다.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

다단계 import 를 사용하는 대신.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
