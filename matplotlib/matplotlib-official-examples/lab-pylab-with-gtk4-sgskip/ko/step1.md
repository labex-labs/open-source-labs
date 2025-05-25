# 필요한 라이브러리 임포트

```python
import matplotlib
matplotlib.use('GTK4Agg')
import gi
import matplotlib.pyplot as plt

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
```

`matplotlib`, `gi`, `pyplot`, 그리고 `Gtk`를 포함한 필요한 라이브러리를 임포트합니다. matplotlib 의 백엔드를 GTK4 를 사용하도록 설정합니다.
