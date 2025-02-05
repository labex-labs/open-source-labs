# 下载数据并创建缺失值数据集

首先，下载这两个数据集。为了加快计算速度，对于加利福尼亚住房数据集，我们仅使用前400个条目。然后，我们将删除一些值，以创建具有人为缺失数据的新版本。

```python
import numpy as np
from sklearn.datasets import fetch_california_housing, load_diabetes

rng = np.random.RandomState(42)

X_diabetes, y_diabetes = load_diabetes(return_X_y=True)
X_california, y_california = fetch_california_housing(return_X_y=True)
X_california = X_california[:400]
y_california = y_california[:400]
X_diabetes = X_diabetes[:400]
y_diabetes = y_diabetes[:400]

def add_missing_values(X_full, y_full):
    n_samples, n_features = X_full.shape

    # 在75%的行中添加缺失值
    missing_rate = 0.75
    n_missing_samples = int(n_samples * missing_rate)

    missing_samples = np.zeros(n_samples, dtype=bool)
    missing_samples[:n_missing_samples] = True

    rng.shuffle(missing_samples)
    missing_features = rng.randint(0, n_features, n_missing_samples)
    X_missing = X_full.copy()
    X_missing[missing_samples, missing_features] = np.nan
    y_missing = y_full.copy()

    return X_missing, y_missing

X_miss_california, y_miss_california = add_missing_values(X_california, y_california)
X_miss_diabetes, y_miss_diabetes = add_missing_values(X_diabetes, y_diabetes)
```
