# 필요한 라이브러리 가져오기 및 데이터 생성

첫 번째 단계는 필요한 라이브러리를 가져오고 데이터를 생성하는 것입니다. 데이터 생성 및 시각화를 위해 numpy 와 matplotlib 를 사용하고, 일원 SVM 모델 구축을 위해 scikit-learn 을 사용합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 학습 데이터 생성
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# 일반적인 새로운 관측치 생성
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# 비정상적인 새로운 관측치 생성
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
