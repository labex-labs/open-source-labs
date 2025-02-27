# 多項式特徴量の生成

時には、入力データの非線形特徴量を考慮することでモデルに複雑さを追加することが有益です。scikit-learn の `PolynomialFeatures` を使って多項式特徴量を生成することができます。

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Create a sample dataset
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# Initialize the PolynomialFeatures
poly = PolynomialFeatures(2)

# Fit and transform the training data
X_poly = poly.fit_transform(X)

# Print the transformed data
print(X_poly)
```
