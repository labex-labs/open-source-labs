# ライブラリのインポート

最初のステップは、必要なライブラリをインポートすることです。Matplotlib、wxPython、NumPy を使用します。Matplotlib は Python 用のグラフ描画ライブラリで、wxPython は Python 用の GUI ツールキットで、NumPy は Python での数値計算用のライブラリです。

```python
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
```
