# Encodage des caractéristiques catégorielles

Les caractéristiques catégorielles doivent être encodées en valeurs numériques avant d'être utilisées dans les algorithmes de machine learning. Nous pouvons utiliser l'`OrdinalEncoder` et l'`OneHotEncoder` de scikit-learn pour encoder les caractéristiques catégorielles.

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
