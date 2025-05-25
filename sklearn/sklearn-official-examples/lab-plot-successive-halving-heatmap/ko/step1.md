# 필요한 라이브러리 및 데이터셋 가져오기

먼저 이 실험에 필요한 라이브러리와 데이터셋을 가져옵니다. 합성 데이터셋을 생성하고 매개변수 검색을 수행하기 위해 scikit-learn 라이브러리를 사용할 것입니다.

```python
from time import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV

rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=1000, random_state=rng)

gammas = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
Cs = [1, 10, 100, 1e3, 1e4, 1e5]
param_grid = {"gamma": gammas, "C": Cs}

clf = SVC(random_state=rng)
```
