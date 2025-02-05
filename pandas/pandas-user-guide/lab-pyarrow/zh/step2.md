# 数据结构集成

PyArrow 允许 pandas 数据结构直接由 PyArrow ChunkedArray 支持，类似于 NumPy 数组。以下是实现方法：

```python
# 导入 pandas
import pandas as pd

# 使用 PyArrow 数据类型创建一个 pandas Series、Index 和 DataFrame
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
