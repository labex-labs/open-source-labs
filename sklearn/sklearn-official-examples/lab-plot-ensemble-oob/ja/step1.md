# 必要なライブラリをインポートする

scikit - learn、NumPy、Matplotlibを含む必要なライブラリをインポートして始めます。再現性を保証するために、乱数シード値も設定します。

```python
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 123
```
