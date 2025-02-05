# 导入所需的库

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

我们导入所需的库，包括 `matplotlib`、`gi`、`pyplot` 和 `Gtk`。我们将 matplotlib 的后端设置为使用 GTK4。
