# Bibliotheken importieren

Der erste Schritt besteht darin, die erforderlichen Bibliotheken zu importieren. Wir werden Matplotlib, wxPython und NumPy verwenden. Matplotlib ist eine Plotbibliothek für Python, wxPython ist ein GUI-Toolkit für Python und NumPy ist eine Bibliothek für numerische Berechnungen mit Python.

```python
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
```
