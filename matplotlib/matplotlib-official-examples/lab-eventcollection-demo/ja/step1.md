# 必要なライブラリをインポートする

まず、必要なライブラリをインポートする必要があります。乱数データを作成するために `numpy` を、グラフを作成するために `matplotlib.pyplot` を、そしてデータポイントの位置をマークするために `matplotlib.collections` からの `EventCollection` を使用します。

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import EventCollection
```
