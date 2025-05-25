# 라이브러리 가져오기

이 실습에서는 필요한 라이브러리를 가져오는 것으로 시작합니다. scikit-learn 라이브러리를 사용하여 데이터셋을 가져오고, 모델을 학습시키며, 모델의 성능을 평가합니다.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```
