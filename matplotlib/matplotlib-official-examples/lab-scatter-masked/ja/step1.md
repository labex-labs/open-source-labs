# 必要なライブラリのインポートと乱数シードの設定

必要なライブラリをインポートし、再現性を保証するために乱数シードを設定して始めます。

```python
import matplotlib.pyplot as plt
import numpy as np

# Setting random seed for reproducibility
np.random.seed(19680801)
```
