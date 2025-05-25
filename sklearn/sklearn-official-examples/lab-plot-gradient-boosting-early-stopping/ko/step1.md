# 필요한 라이브러리 및 데이터 로드

먼저, 필요한 라이브러리와 데이터를 로드해야 합니다. 경사 부스팅 구현에는 scikit-learn 라이브러리를 사용할 것입니다.

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn import datasets
from sklearn.model_selection import train_test_split

data_list = [
    datasets.load_iris(return_X_y=True),
    datasets.make_classification(n_samples=800, random_state=0),
    datasets.make_hastie_10_2(n_samples=2000, random_state=0),
]
names = ["Iris Data", "Classification Data", "Hastie Data"]
n_estimators = 200
```
