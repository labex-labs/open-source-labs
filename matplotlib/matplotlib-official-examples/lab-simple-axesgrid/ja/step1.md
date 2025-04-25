# 必要なライブラリをインポートして画像配列を作成する

まず、必要なライブラリをインポートし、NumPy ライブラリの`arange`関数と`reshape`関数を使って 4 つの 10x10 の画像配列を作成します。

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
