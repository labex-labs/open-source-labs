# ブロードキャスト

ブロードキャストは、ufuncの強力な機能であり、異なる形状の配列に対して演算を行うことができます。ブロードキャスト規則は、演算中に異なる形状の配列がどのように扱われるかを決定します。例を見てみましょう。

```python
import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])

# Multiply the arrays
result = arr1 * arr2

# Print the result
print(result)
```

出力:

```
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```
