# ライブラリのインポート

まず、必要なライブラリをインポートする必要があります。Matplotlib、GTK3、および gi.repository からの Gtk モジュールを使用します。

```python
import matplotlib
matplotlib.use('GTK3Agg')  # または 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
