# 从磁盘读取数组

你可以以各种格式从磁盘读取数组。对于标准二进制格式，有像用于 HDF5 的 h5py 和用于 FITS 的 Astropy 这样的 Python 库。对于像 CSV 和 TSV 这样的常见 ASCII 格式，你可以使用 `np.loadtxt` 和 `np.genfromtxt` 函数。以下是读取 CSV 文件的示例：

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
