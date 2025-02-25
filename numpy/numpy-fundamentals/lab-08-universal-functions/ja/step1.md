# 基本的な算術演算

基本的なufuncはスカラーに対して動作し、最も単純な例は加算演算子です。要素ごとに2つの配列を加算するには、加算演算子をどのように使用するか見てみましょう。

```python
import numpy as np

# Create two arrays
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# Add the arrays element-wise
result = arr1 + arr2

# Print the result
print(result)
```

出力:

```
array([1, 3, 2, 6])
```
