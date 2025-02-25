# ライブラリのインポートとデータの生成

まず、必要なライブラリをインポートして、プロットするためのデータを生成する必要があります。この例では、正規分布を使ってy軸用のデータを生成します。

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
```
