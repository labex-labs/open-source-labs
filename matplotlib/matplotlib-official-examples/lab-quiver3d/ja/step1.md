# ライブラリのインポートとプロットの設定

最初のステップは、必要なライブラリをインポートしてプロットを設定することです。この例では、3D プロットを作成するために Matplotlib の`pyplot`モジュールとその`3d`ツールキットを使用します。

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
