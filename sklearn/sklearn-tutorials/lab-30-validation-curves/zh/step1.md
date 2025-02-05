# 导入所需库并加载数据

让我们先导入必要的库并加载一个数据集。在这个例子中，我们将使用鸢尾花数据集。

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```
