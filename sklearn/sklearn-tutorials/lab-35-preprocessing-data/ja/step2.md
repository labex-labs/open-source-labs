# スケーリング

特徴量を特定の範囲にスケーリングすることは、もう一つの一般的な前処理手法です。特徴量が異なるスケールを持っており、同じ範囲にする必要がある場合に便利です。`MinMaxScaler` と `MaxAbsScaler` を使ってスケーリングを行うことができます。

```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the MinMaxScaler
min_max_scaler = MinMaxScaler()

# Fit and transform the training data
X_minmax = min_max_scaler.fit_transform(X)

# Print the transformed data
print(X_minmax)

# Initialize the MaxAbsScaler
max_abs_scaler = MaxAbsScaler()

# Fit and transform the training data
X_maxabs = max_abs_scaler.fit_transform(X)

# Print the transformed data
print(X_maxabs)
```
