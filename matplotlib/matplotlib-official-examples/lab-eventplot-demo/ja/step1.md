# ライブラリのインポートと乱数シードの設定

必要なライブラリをインポートし、再現性のために乱数シードを設定して始めましょう。

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)
```
