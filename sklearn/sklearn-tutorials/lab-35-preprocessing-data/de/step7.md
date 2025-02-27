# Erstellen benutzerdefinierter Transformatoren

In einigen Fällen möchten wir eine vorhandene Python-Funktion in einen Transformator umwandeln, um die Datenbereinigung oder -verarbeitung zu erleichtern. Wir können dies mit dem `FunctionTransformer` aus scikit-learn erreichen.

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
