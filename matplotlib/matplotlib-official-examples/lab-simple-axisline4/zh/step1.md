# 导入必要的模块

第一步是导入绘制图表所需的必要模块。我们将使用`numpy`生成x和y数据，使用`matplotlib.pyplot`创建图表，并使用`mpl_toolkits.axes_grid1`创建第二个y轴。

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
```
