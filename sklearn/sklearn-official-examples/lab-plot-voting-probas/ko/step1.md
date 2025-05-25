# 분류기 및 데이터셋 초기화

먼저 세 가지 분류기와 하나의 예제 데이터셋을 초기화합니다. LogisticRegression, GaussianNB, 그리고 RandomForestClassifier 를 분류기로 사용하고, X 와 y 를 예제 데이터셋으로 사용합니다.

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

clf1 = LogisticRegression(max_iter=1000, random_state=123)
clf2 = RandomForestClassifier(n_estimators=100, random_state=123)
clf3 = GaussianNB()
X = np.array([[-1.0, -1.0], [-1.2, -1.4], [-3.4, -2.2], [1.1, 1.2]])
y = np.array([1, 1, 2, 2])
```
