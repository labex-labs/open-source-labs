# 라이브러리 임포트

첫 번째 단계는 필요한 라이브러리를 임포트하는 것입니다. Matplotlib, wxPython 및 NumPy 를 사용할 것입니다. Matplotlib 은 Python 용 플로팅 라이브러리이고, wxPython 은 Python 용 GUI 툴킷이며, NumPy 는 Python 을 사용한 수치 계산을 위한 라이브러리입니다.

```python
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
```
