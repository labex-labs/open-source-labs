# 필요한 패키지 가져오기

첫 번째 단계는 프로젝트에 필요한 패키지를 가져오는 것입니다.

```python
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg as NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.contour import ContourSet
import sys
import numpy as np
import tkinter as Tk
from sklearn import svm
from sklearn.datasets import dump_svmlight_file
```
