# 必要なライブラリとデータセットをインポートする

まず、必要なライブラリをインポートして、バイクラスタリングに使用するサンプルデータセットを読み込みましょう。

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Load sample data
data = np.arange(100).reshape(10, 10)
```
