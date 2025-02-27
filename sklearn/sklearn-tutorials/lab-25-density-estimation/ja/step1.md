# 必要なライブラリをインポートする

まず、密度推定に使用するライブラリをインポートする必要があります。密度推定には、`sklearn.neighbors` モジュールの `KernelDensity` 推定器と、データ操作に `numpy` ライブラリを使用します。

```python
from sklearn.neighbors import KernelDensity
import numpy as np
```
