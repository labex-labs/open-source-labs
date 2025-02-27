# Kodierung kategorischer Merkmale

Kategorische Merkmale müssen in numerische Werte kodiert werden, bevor sie in Machine-Learning-Algorithmen verwendet werden können. Wir können den `OrdinalEncoder` und den `OneHotEncoder` aus scikit-learn verwenden, um kategorische Merkmale zu kodieren.

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
