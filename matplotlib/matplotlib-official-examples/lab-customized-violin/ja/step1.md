# テストデータを作成する

まず、バイオリンプロットに使用するためのテストデータを作成します。標準偏差が増加する100個の正規分布の値を持つ4つの配列を生成するためにNumPyを使用します。

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
