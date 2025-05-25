# 모델 학습

훈련 데이터로 Isolation Forest 모델을 학습합니다.

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
