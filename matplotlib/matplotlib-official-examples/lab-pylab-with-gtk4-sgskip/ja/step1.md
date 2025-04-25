# 必要なライブラリをインポートする

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

`matplotlib`、`gi`、`pyplot`、および`Gtk`を含む必要なライブラリをインポートします。matplotlib のバックエンドを GTK4 を使用するように設定します。
