# ライブラリのインポートと乱数シードの設定

必要なライブラリをインポートし、結果の再現性を保証するために乱数シードを設定します。

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random seed
np.random.seed(19680801)
```
