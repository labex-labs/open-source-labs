# 라이브러리 가져오기 및 합성 데이터셋 생성

L1 및 L2 정규화에 적합한 합성 데이터셋을 생성하여 시작합니다.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.svm import LinearSVC
from sklearn.model_selection import validation_curve, ShuffleSplit

n_samples, n_features = 100, 300
X, y = make_classification(n_samples=n_samples, n_features=n_features, n_informative=5, random_state=1)

rng = np.random.RandomState(1)
y = np.sign(0.5 - rng.rand(n_samples))
X = rng.randn(n_samples, n_features // 5) + y[:, np.newaxis]
X += 5 * rng.randn(n_samples, n_features // 5)
```
