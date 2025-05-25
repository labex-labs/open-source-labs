# 라이브러리 임포트

먼저, 필요한 라이브러리를 임포트해야 합니다. Matplotlib, GTK3, 그리고 gi.repository 에서 Gtk 모듈을 사용할 것입니다.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # or 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
