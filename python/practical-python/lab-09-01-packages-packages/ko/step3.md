# 패키지 사용하기 (Using a Package)

패키지는 import 를 위한 네임스페이스 (namespace) 역할을 합니다.

이는 이제 다단계 import 가 있다는 것을 의미합니다.

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

import 문에는 다른 변형이 있습니다.

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
