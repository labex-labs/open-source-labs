# 导入库

第一步是导入必要的库。我们将使用 Matplotlib、wxPython 和 NumPy。Matplotlib 是一个用于 Python 的绘图库，wxPython 是一个用于 Python 的 GUI 工具包，NumPy 是一个用于 Python 数值计算的库。

```python
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
```
