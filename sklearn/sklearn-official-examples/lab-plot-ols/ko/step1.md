# 당뇨병 데이터셋 로드

scikit-learn 에서 당뇨병 데이터셋을 로드하고 데이터셋에서 하나의 특징만 선택하여 시작합니다.

```python
import numpy as np
from sklearn import datasets

# 당뇨병 데이터셋 로드
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# 하나의 특징만 사용
diabetes_X = diabetes_X[:, np.newaxis, 2]
```
