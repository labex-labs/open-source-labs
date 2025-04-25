# ランダムデータの生成

まず、0 から 1 の間の 1000 個のランダムな数を含む 100 のランダムなデータセットを生成する必要があります。ランダムデータを生成するために、numpy の random モジュールを使用します。

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
