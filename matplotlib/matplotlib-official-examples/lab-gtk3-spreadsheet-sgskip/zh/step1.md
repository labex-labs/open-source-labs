# 设置环境

在开始之前，我们需要设置我们的环境。我们将首先创建一个新的 Python 文件并导入必要的库。

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
