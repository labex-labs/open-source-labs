# 导入库

在这一步中，我们将导入分析所需的库。我们将导入用于机器学习的scikit-learn库、用于数值计算的numpy库以及用于可视化的matplotlib库。

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```
