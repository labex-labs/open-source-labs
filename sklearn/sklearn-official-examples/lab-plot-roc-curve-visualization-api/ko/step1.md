# 데이터 로드 및 SVC 학습

먼저 와인 데이터셋을 로드하고 이를 이진 분류 문제로 변환합니다. 그런 다음 훈련 데이터셋에 서포트 벡터 분류기를 학습시킵니다.

```python
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import RocCurveDisplay
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y=True)
y = y == 2

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
svc = SVC(random_state=42)
svc.fit(X_train, y_train)
```
