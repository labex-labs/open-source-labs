# 导入所需库

本实验将使用以下库：`pandas`、`numpy`、`matplotlib`、`sklearn.datasets`、`RandomForestClassifier`、`randint` 和 `HalvingRandomSearchCV`。使用以下代码导入它们：

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV
```
