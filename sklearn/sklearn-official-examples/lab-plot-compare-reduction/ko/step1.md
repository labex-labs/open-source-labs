# 필요한 라이브러리 가져오기 및 데이터 로드

필요한 라이브러리를 가져오고 scikit-learn 에서 숫자 데이터셋을 로드하는 것으로 시작합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA, NMF
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.preprocessing import MinMaxScaler

X, y = load_digits(return_X_y=True)
```
