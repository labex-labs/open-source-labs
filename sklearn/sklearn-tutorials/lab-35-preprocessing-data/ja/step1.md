# 標準化

標準化は、多くの機械学習アルゴリズムに共通する前処理ステップです。これは、特徴量を平均 0、分散 1 に変換します。scikit-learn の `StandardScaler` を使って標準化を行うことができます。

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler on the training data
scaler.fit(X)

# Transform the training data
X_scaled = scaler.transform(X)

# Print the transformed data
print(X_scaled)
```
