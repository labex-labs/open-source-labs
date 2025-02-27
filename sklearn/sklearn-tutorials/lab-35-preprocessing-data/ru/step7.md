# Создание пользовательских трансформеров

В некоторых случаях мы можем захотеть преобразовать существующую функцию на Python в трансформер, чтобы помочь в очистке или обработке данных. Мы можем это сделать с использованием `FunctionTransformer` из scikit-learn.

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
