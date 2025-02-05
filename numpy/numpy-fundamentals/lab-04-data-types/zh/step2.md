# 使用数据类型

NumPy 数据类型由 `dtype`（数据类型）对象表示。使用 `import numpy as np` 导入 NumPy 后，你可以通过 `np.bool_`、`np.float32` 等访问数据类型。

你可以将数据类型用作函数，将 Python 数字转换为数组标量，将 Python 数字序列转换为该类型的数组，或者在许多 NumPy 函数或方法中作为 `dtype` 关键字的参数。以下是一些示例：

```python
x = np.float32(1.0)
# x 现在是一个值为 1.0 的 float32 数组标量

y = np.int_([1,2,4])
# y 现在是一个值为 [1, 2, 4] 的 int 数组

z = np.arange(3, dtype=np.uint8)
# z 现在是一个值为 [0, 1, 2] 的 uint8 数组
```

你也可以使用字符代码引用数组类型，不过建议使用 `dtype` 对象。例如：

```python
np.array([1, 2, 3], dtype='f')
# 返回一个值为 [1., 2., 3.] 且数据类型为 float32 的数组
```

要转换数组的类型，可以使用 `.astype()` 方法，也可以将类型本身用作函数。例如：

```python
z.astype(float)
# 返回数据类型为 float64 的数组 z

np.int8(z)
# 返回数据类型为 int8 的数组 z
```
