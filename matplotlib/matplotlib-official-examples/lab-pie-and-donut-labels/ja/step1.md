# 必要なライブラリをインポートしてサブプロット付きのグラフを作成する

まずは必要なライブラリをインポートして、サブプロット付きのグラフを作成します。

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
