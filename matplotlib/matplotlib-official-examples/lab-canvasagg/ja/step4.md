# レンダラーバッファをnumpy配列に抽出する

グラフを保存する2番目のオプションは、レンダラーバッファをnumpy配列に抽出することです。これにより、cgiスクリプト内でMatplotlibを使用して、グラフをディスクに書き込む必要なく済みます。この例では、レンダラーバッファを抽出してnumpy配列に変換します。

```python
import numpy as np

canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```
