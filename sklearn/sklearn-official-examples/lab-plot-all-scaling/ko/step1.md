# 라이브러리 및 데이터셋 가져오기

먼저 필요한 라이브러리를 가져오고 scikit-learn 에서 캘리포니아 주택 데이터셋을 로드해야 합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
from sklearn.datasets import fetch_california_housing

# 캘리포니아 주택 데이터셋 로드
dataset = fetch_california_housing()
X_full, y_full = dataset.data, dataset.target
feature_names = dataset.feature_names
```
