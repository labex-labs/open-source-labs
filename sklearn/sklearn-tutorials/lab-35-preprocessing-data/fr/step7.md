# Création de transformateurs personnalisés

Dans certains cas, nous pouvons vouloir convertir une fonction Python existante en un transformateur pour faciliter le nettoyage ou le traitement des données. Nous pouvons le faire à l'aide du `FunctionTransformer` de scikit-learn.

```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

# Create a custom function
def custom_function(X):
    return np.log1p(X)

# Initialize the FunctionTransformer
transformer = FunctionTransformer(custom_function)

# Create a sample dataset
X = np.array([[0, 1],
              [2, 3]])

# Transform the data using the custom function
X_transformed = transformer.transform(X)

# Print the transformed data
print
```
