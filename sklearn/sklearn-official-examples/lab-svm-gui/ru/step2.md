# Импорт необходимых пакетов

Первым шагом является импорт необходимых пакетов для проекта.

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
