# 必要なライブラリをインポートする

まず、Matplotlib、NumPy、Matplotlib フォントマネージャ、および mpl_toolkits.axes_grid1 からの AnchoredDirectionArrows などの必要なライブラリをインポートする必要があります。これらのライブラリを使用して固定方向矢印を作成します。

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows
```
