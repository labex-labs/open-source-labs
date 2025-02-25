# 必要なライブラリをインポートする

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

`matplotlib`、`gi`、`pyplot`、および`Gtk`を含む必要なライブラリをインポートします。matplotlibのバックエンドをGTK4を使用するように設定します。
