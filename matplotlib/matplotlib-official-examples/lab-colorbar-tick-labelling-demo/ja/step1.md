# 必要なライブラリをインポートして乱数シードを固定する

まず、再現性のために必要なライブラリをインポートして乱数シードを固定する必要があります。乱数データを生成するために `numpy` を、ビジュアライゼーションを作成するために `matplotlib.pyplot` を、カラーマップを定義するために `matplotlib` の `cm` を使用します。

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
