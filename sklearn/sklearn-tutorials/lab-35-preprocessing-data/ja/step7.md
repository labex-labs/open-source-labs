# カスタムトランスフォーマーの作成

場合によっては、既存のPython関数をトランスフォーマーに変換して、データのクリーニングや処理を支援したい場合があります。これは、scikit-learnの `FunctionTransformer` を使用して達成できます。

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
