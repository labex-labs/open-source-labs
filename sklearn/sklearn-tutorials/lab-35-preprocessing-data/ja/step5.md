# 欠損値の補完

データセットにおける欠損値は、機械学習アルゴリズムに問題を引き起こす可能性があります。scikit-learn の `impute` モジュールに提供されているメソッドを使って欠損値を処理することができます。ここでは、欠損値を補完するために `SimpleImputer` を使用します。

```python
from sklearn.impute import SimpleImputer
import numpy as np

# Create a sample dataset with missing values
X = np.array([[1., 2., np.nan],
              [3., np.nan, 5.],
              [np.nan, 4., 6.]])

# Initialize the SimpleImputer
imputer = SimpleImputer()

# Fit and transform the training data
X_imputed = imputer.fit_transform(X)

# Print the transformed data
print(X_imputed)
```
