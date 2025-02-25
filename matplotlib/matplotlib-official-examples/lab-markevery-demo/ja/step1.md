# データポイントを定義する

まず、プロットに使用するデータポイントを定義します。この例では、`numpy` を使ってサイン波の一連の x と y の値を生成します。

```python
import matplotlib.pyplot as plt
import numpy as np

# プロットする markevery のケースのリストを定義する
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 32],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.4,
    (0.2, 0.4)
]

# データポイント
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
```
