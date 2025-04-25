# レンダラーバッファを numpy 配列に抽出する

グラフを保存する 2 番目のオプションは、レンダラーバッファを numpy 配列に抽出することです。これにより、cgi スクリプト内で Matplotlib を使用して、グラフをディスクに書き込む必要なく済みます。この例では、レンダラーバッファを抽出して numpy 配列に変換します。

```python
import numpy as np

canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```
