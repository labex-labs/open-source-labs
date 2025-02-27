# 必要なライブラリをインポートする

必要なライブラリをインポートして始めましょう。これには、`sklearn.datasets` からの `make_gaussian_quantiles` と `accuracy_score`、`sklearn.ensemble` からの `AdaBoostClassifier`、`DecisionTreeClassifier`、および `matplotlib.pyplot` が含まれます。

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
```
