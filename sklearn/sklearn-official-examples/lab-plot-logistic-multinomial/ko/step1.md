# 라이브러리 가져오기

이 실습에서는 필요한 라이브러리를 가져오는 것으로 시작합니다. scikit-learn 라이브러리를 사용하여 데이터셋을 생성하고 로지스틱 회귀 모델을 학습하며, matplotlib 라이브러리를 사용하여 결정 경계를 시각화합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```
