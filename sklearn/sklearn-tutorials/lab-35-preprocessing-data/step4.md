# Encoding Categorical Features

Categorical features need to be encoded into numerical values before they can be used in machine learning algorithms. We can use the `OrdinalEncoder` and `OneHotEncoder` from scikit-learn to encode categorical features.

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
