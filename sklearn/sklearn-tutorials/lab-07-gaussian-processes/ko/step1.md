# 가우시안 프로세스 회귀 (GPR)

GaussianProcessRegressor 클래스는 회귀 작업을 위한 가우시안 프로세스를 구현합니다. GP 에 대한 사전 (prior) 을 지정해야 하며, 이는 평균 및 공분산 함수와 같습니다. 커널의 하이퍼파라미터는 맞춤 과정에서 최적화됩니다. GPR 을 회귀에 사용하는 예를 살펴보겠습니다.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# RBF 커널을 사용하여 GPR 모델 생성
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# 학습 데이터에 모델 적합
model.fit(X_train, y_train)

# 학습된 모델을 사용하여 예측
y_pred = model.predict(X_test)
```
