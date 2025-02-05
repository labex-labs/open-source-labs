# 导入必要的库并创建带有子图的图形

我们首先导入必要的库并创建一个带有子图的图形。

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
