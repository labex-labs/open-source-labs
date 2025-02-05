# 导入所需库

我们将首先导入所需的库，包括来自`sklearn.datasets`的`make_gaussian_quantiles`和`accuracy_score`，来自`sklearn.ensemble`的`AdaBoostClassifier`、`DecisionTreeClassifier`，以及`matplotlib.pyplot`。

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
```
