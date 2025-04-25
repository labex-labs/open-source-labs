# ライブラリとデータセットのインポート

まず、必要なライブラリとデータセットをインポートする必要があります。この例では、3 次元プロットを作成するために`matplotlib`と`mpl_toolkits.mplot3d`ライブラリを使用し、サンプルデータセットを生成するために`axes3d.get_test_data()`関数を使用します。

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Generate sample dataset
X, Y, Z = axes3d.get_test_data(0.05)
```
