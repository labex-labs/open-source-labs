# 必要なライブラリをインポートしてデータを作成する

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

まず、必要なライブラリ、つまりMatplotlibとNumPyをインポートします。そして、描画するデータを作成します。この例では、numpy配列「t」を作成し、tを使って別のnumpy配列「s」を計算します。
