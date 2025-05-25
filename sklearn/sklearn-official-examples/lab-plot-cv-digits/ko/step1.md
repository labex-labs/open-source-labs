# 데이터셋 로드

먼저, scikit-learn 에서 숫자 데이터셋을 로드하고 특징 (features) 과 레이블 (labels) 로 분할해야 합니다.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
