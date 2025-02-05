# 创建图表

现在我们可以开始创建图表了。首先，导入必要的库并定义 `Window1Signals` 类。这个类将处理窗口的 `destroy` 信号。

```python
from pathlib import Path

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import numpy as np

from matplotlib.backends.backend_gtk3agg import \
    FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure


class Window1Signals:
    def on_window1_destroy(self, widget):
        Gtk.main_quit()
```
