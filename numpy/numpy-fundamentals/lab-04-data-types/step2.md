# Working with Data Types

NumPy data types are represented as `dtype` (data-type) objects. Once you have imported NumPy using `import numpy as np`, you can access the data types using `np.bool_`, `np.float32`, etc.

You can use data types as functions to convert Python numbers to array scalars, Python sequences of numbers to arrays of that type, or as arguments to the dtype keyword in many NumPy functions or methods. Here are some examples:

```python
x = np.float32(1.0)
# x is now a float32 array scalar with value 1.0

y = np.int_([1,2,4])
# y is now an int array with values [1, 2, 4]

z = np.arange(3, dtype=np.uint8)
# z is now a uint8 array with values [0, 1, 2]
```

You can also refer to array types using character codes, although it is recommended to use dtype objects instead. For example:

```python
np.array([1, 2, 3], dtype='f')
# returns an array with values [1., 2., 3.] and dtype float32
```

To convert the type of an array, you can use the `.astype()` method or the type itself as a function. For example:

```python
z.astype(float)
# returns the array z with dtype float64

np.int8(z)
# returns the array z with dtype int8
```
