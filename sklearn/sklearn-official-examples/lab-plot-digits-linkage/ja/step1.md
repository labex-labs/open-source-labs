# ライブラリのインポート

この実験に必要なライブラリをインポートして始めましょう。凝集型クラスタリングを実行するために、numpy、matplotlib、manifold、およびscikit-learnのdatasetsを使用します。

```python
import numpy as np
from matplotlib import pyplot as plt
from time import time
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering
```
