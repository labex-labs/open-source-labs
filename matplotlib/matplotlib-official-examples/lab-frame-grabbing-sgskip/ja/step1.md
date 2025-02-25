# 必要なライブラリをインポートする

まず、アニメーションを生成するために必要なライブラリをインポートします。乱数の生成には`numpy`、グラフ描画には`matplotlib`、フレームをファイルに書き込むためには`FFMpegWriter`を使用します。

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
