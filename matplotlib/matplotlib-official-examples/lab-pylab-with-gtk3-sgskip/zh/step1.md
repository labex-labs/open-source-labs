# 导入库

首先，我们需要导入必要的库。我们将使用Matplotlib、GTK3以及来自gi.repository的Gtk模块。

```python
import matplotlib
matplotlib.use('GTK3Agg')  # 或者 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
