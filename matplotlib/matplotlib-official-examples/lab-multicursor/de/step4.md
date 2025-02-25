# Hinzufügen des MultiCursors

Schließlich werden wir die `MultiCursor`-Funktion hinzufügen, um einen Cursor auf allen drei Diagrammen anzuzeigen, wenn über einem Datenpunkt gehovered wird.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```

需要注意的是，这里的`MultiCursor`前面应该先定义过，不然代码会报错，因为`MultiCursor`是`matplotlib.widgets`模块下的函数，使用前需要导入该模块，完整代码示例如下：

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import MultiCursor

t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)

multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```

以上是完整的翻译及代码说明，确保在运行代码前正确导入所需模块。
