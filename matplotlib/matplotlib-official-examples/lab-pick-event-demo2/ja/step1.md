# ランダムデータの生成

まず、0から1の間の1000個のランダムな数を含む100のランダムなデータセットを生成する必要があります。ランダムデータを生成するために、numpyのrandomモジュールを使用します。

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
