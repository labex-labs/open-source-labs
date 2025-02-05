# 导入库并获取框体样式

在这一步中，我们将导入必要的库，并获取用于绘图的框体样式。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```
