# 正規化

正規化は、個々のサンプルを単位ノルムにスケーリングするプロセスです。データの大きさが重要でなく、データの方向（または角度）のみに興味がある場合に一般的に使用されます。scikit-learn の `Normalizer` を使って正規化を行うことができます。

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the Normalizer
normalizer = Normalizer()

# Fit and transform the training data
X_normalized = normalizer.fit_transform(X)

# Print the transformed data
print(X_normalized)
```
