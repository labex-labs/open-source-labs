# 在运行时设置 rcParams

你可以在 Python 脚本中动态更改默认的运行时配置设置，也可以在 Python shell 中进行交互式更改。`matplotlib.rcParams`变量是 Matplotlib 包的全局变量，用于存储所有的 rc 设置。要在运行时自定义 rcParams，你可以直接使用`mpl.rcParams`字典进行修改。以下是一个示例：

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

这段代码更改了使用 Matplotlib 创建的所有图表的默认线宽和线型。

让我们看看使用新默认设置绘制的一些随机数据。

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
