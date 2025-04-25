# 環境をセットアップする

始める前に、環境をセットアップする必要があります。まず新しい Python ファイルを作成し、必要なライブラリをインポートします。

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
