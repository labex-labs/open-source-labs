# Python 패키지 및 데이터셋 가져오기, 데이터셋 로드

```python
# 표준 과학 Python 가져오기
import matplotlib.pyplot as plt
import numpy as np
from time import time

# 데이터셋, 분류기 및 성능 지표 가져오기
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# 숫자 데이터셋
digits = datasets.load_digits(n_class=9)
```
