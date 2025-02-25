# 必要なライブラリをインポートして関数を定義する

必要なライブラリをインポートし、最初の画像を作成する関数を定義します。

```python
import matplotlib.pyplot as plt
import numpy as np

def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))
```
