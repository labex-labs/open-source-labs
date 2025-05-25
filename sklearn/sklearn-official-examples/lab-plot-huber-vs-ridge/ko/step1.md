# 필요한 라이브러리 가져오기

데이터 조작 및 시각화를 위해 numpy 와 matplotlib, 그리고 회귀 모델링을 위해 scikit-learn 의 HuberRegressor 와 Ridge 를 포함한 필요한 라이브러리를 가져옵니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import HuberRegressor, Ridge
```
