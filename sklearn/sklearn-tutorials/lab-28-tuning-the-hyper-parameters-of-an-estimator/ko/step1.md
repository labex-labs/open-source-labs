# 필요한 라이브러리 가져오기

먼저, 분석에 필요한 라이브러리를 가져와야 합니다. 하이퍼파라미터 튜닝을 위해 `sklearn.model_selection`을 사용할 것입니다.

```python
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
```
