# 환경 설정

시작하기 전에 환경을 설정해야 합니다. 새로운 Python 파일을 생성하고 필요한 라이브러리를 임포트 (import) 하는 것으로 시작합니다.

```python
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from numpy.random import random
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.figure import Figure
```
