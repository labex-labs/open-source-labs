# 데이터셋 로드

scikit-learn 의 `load_digits()` 함수를 사용하여 숫자 데이터셋을 로드합니다. 이 함수는 데이터셋의 특징과 레이블을 반환합니다.

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
