# 导入必要的库和数据集

首先，让我们导入必要的库，并加载一个将用于双聚类的示例数据集。

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Load sample data
data = np.arange(100).reshape(10, 10)
```
