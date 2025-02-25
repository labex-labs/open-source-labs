# 画像データのインポート

まず、必要なライブラリをインポートし、画像データを NumPy 配列に読み込む必要があります。この例では、`PIL` ライブラリを使って画像を読み込み、その後 NumPy 配列に変換します。

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
