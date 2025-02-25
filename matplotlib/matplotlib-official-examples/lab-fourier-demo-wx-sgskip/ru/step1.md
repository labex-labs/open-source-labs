# Импорт библиотек

Первым шагом является импорт необходимых библиотек. Мы будем использовать Matplotlib, wxPython и NumPy. Matplotlib - это библиотека для построения графиков в Python, wxPython - это инструмент для создания графического интерфейса пользователя (GUI) в Python, а NumPy - это библиотека для численных вычислений с использованием Python.

```python
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
```
