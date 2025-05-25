# 필요한 라이브러리 가져오기 및 데이터 로드

필요한 라이브러리를 가져오고 scikit-learn 에서 숫자 데이터셋을 로드하는 것으로 시작합니다.

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# 숫자 데이터셋 로드
X, y = load_digits(return_X_y=True, n_class=3)
```
