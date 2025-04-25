# Ufunc メソッド

Ufunc には、reduce、accumulate、reduceat、outer の 4 つのメソッドがあります。これらのメソッドは、配列に対する操作を行う際に便利です。まずは、reduce メソッドを見てみましょう。

```python
import numpy as np

# Create an array
arr = np.arange(9).reshape(3, 3)

# Reduce the array along the first axis
result = np.add.reduce(arr, 1)

# Print the result
print(result)
```

出力：

```
array([ 3, 12, 21])
```
