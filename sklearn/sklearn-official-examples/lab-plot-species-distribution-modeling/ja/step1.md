# ライブラリのインポート

このステップでは、分析に必要なライブラリをインポートします。機械学習のためのscikit-learnライブラリ、数値計算のためのnumpy、可視化のためのmatplotlibをインポートします。

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```
