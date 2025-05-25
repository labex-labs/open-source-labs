# 필요한 라이브러리 및 데이터셋 가져오기

먼저, 필요한 라이브러리를 가져오고 scikit-learn 에서 아이리스 데이터셋을 로드합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # 첫 두 개의 특징만 사용합니다.
y = np.array(iris.target, dtype=int)
```
