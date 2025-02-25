# 実行時に rcParams を設定する

Python スクリプト内で、または Python シェルから対話的に、既定の実行時構成設定を動的に変更することができます。`matplotlib.rcParams` 変数は Matplotlib パッケージ全体でグローバルなもので、すべての rc 設定を格納しています。実行時に rcParams をカスタマイズするには、`mpl.rcParams` 辞書を使って直接変更することができます。以下は例です：

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

このコードは、Matplotlib で作成されるすべてのプロットの既定の線幅と線のスタイルを変更します。

新しい既定設定で描画されたいくつかのランダムなデータを見てみましょう。

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
