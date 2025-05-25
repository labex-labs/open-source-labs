# 대역폭 최적화

KDE 의 대역폭 매개변수를 최적화하기 위해 그리드 검색 교차 검증을 사용합니다. 대역폭 매개변수는 밀도 추정의 매끄러움을 제어합니다.

```python
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

# 그리드 검색 교차 검증을 사용하여 대역폭 최적화
params = {"bandwidth": np.logspace(-1, 1, 20)}
grid = GridSearchCV(KernelDensity(), params)
grid.fit(data)

print("최적 대역폭: {0}".format(grid.best_estimator_.bandwidth))

# 최적 추정자를 사용하여 커널 밀도 추정 계산
kde = grid.best_estimator_
```
