# 导入库和数据集

首先，我们需要导入必要的库和数据集。在这个例子中，我们将使用 `matplotlib` 和 `mpl_toolkits.mplot3d` 库来创建3D图，并使用 `axes3d.get_test_data()` 函数生成一个示例数据集。

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
