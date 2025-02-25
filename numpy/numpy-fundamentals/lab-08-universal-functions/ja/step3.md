# 出力型の決定

すべての入力引数がndarrayでない場合、ufuncの出力は必ずしもndarrayではありません。出力型は、入力型と型キャストの規則に基づいて決定できます。例を見てみましょう。

```python
import numpy as np

# Create an array
arr = np.arange(9).reshape(3, 3)

# Perform multiplication and specify the output type
result = np.multiply.reduce(arr, dtype=float)

# Print the result
print(result)
```

出力:

```
array([ 0., 28., 80.])
```
