# 导入库并设置随机种子

我们将首先导入必要的库，并设置一个随机种子以确保可重复性。

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)
```
