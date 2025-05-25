# 데이터 로드

시작하기 전에 아이리스 (Iris) 데이터셋을 로드하고 시각화를 위해 처음 두 개의 특징만 선택합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 0, :2]
y = y[y != 0]
```
