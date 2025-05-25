# 가우시안 프로세스 분류 (GPC)

GaussianProcessClassifier 클래스는 확률적 분류를 위한 GPC 를 구현합니다. 잠재 함수에 GP 사전을 배치한 다음, 연결 함수를 통해 압축하여 클래스 확률을 얻습니다. GPC 는 일대다 또는 일대일 기반의 학습 및 예측을 수행하여 다중 클래스 분류를 지원합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier

# RBF 커널을 사용하여 GPC 모델 생성
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 학습 데이터에 모델 적합
model.fit(X_train, y_train)

# 학습된 모델을 사용하여 예측
y_pred = model.predict(X_test)
```
