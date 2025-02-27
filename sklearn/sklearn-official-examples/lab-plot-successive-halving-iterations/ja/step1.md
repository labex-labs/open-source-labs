# 必要なライブラリのインポート

この実験では、以下のライブラリを使用します：`pandas`、`numpy`、`matplotlib`、`sklearn.datasets`、`RandomForestClassifier`、`randint`、および`HalvingRandomSearchCV`。以下のコードを使ってインポートしましょう：

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
