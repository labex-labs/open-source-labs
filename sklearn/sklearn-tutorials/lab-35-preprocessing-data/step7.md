# Creating Custom Transformers

In some cases, we may want to convert an existing Python function into a transformer to assist in data cleaning or processing. We can achieve this using the `FunctionTransformer` from scikit-learn.

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
