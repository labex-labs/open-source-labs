# カテゴリカル特徴量のエンコード

カテゴリカル特徴量は、機械学習アルゴリズムで使用する前に数値にエンコードする必要があります。scikit-learn の `OrdinalEncoder` と `OneHotEncoder` を使ってカテゴリカル特徴量をエンコードすることができます。

```python
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import numpy as np

# Create a sample dataset
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]

# Initialize the OrdinalEncoder
ordinal_encoder = OrdinalEncoder()

# Fit and transform the training data
X_encoded = ordinal_encoder.fit_transform(X)

# Print the transformed data
print(X_encoded)

# Initialize the OneHotEncoder
onehot_encoder = OneHotEncoder()

# Fit and transform the training data
X_onehot = onehot_encoder.fit_transform(X)

# Print the transformed data
print(X_onehot.toarray())
```
