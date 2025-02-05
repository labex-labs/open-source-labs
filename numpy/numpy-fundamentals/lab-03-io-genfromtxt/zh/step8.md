# 使用快捷函数

`numpy.lib.npyio` 模块提供了从 `numpy.genfromtxt` 派生而来的快捷函数。这些函数具有不同的默认值，并返回标准的 NumPy 数组或掩码数组。

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
