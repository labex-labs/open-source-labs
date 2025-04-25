# ライブラリのインポート

このステップでは、分析に必要なライブラリをインポートします。機械学習のための scikit-learn ライブラリ、数値計算のための numpy、可視化のための matplotlib をインポートします。

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```
