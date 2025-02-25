# Ufuncの動作のオーバーライド

ndarrayサブクラスを含むクラスは、特定の特殊メソッドを定義することで、ufuncがそれらに対してどのように動作するかをオーバーライドすることができます。これにより、ufuncの動作をカスタマイズすることが可能になります。例を見てみましょう。

```python
import numpy as np

# Define a custom class
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Custom add method called")
        return super().__add__(other)

# Create an instance of the custom class
arr = MyArray([1, 2, 3])

# Perform addition
result = arr + 1

# Print the result
print(result)
```

出力:

```
Custom add method called
[2 3 4]
```
