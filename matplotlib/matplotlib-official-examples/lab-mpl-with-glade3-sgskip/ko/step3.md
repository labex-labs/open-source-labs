# 그래프 생성

이제 그래프를 만들기 시작할 수 있습니다. 먼저, 필요한 라이브러리를 import 하고 `Window1Signals` 클래스를 정의합니다. 이 클래스는 창의 `destroy` 시그널을 처리합니다.

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
