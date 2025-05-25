# GPR 예제

잡음 수준 추정이 포함된 GPR: 이 예제는 데이터의 잡음 수준을 추정하기 위해 WhiteKernel 이 포함된 합 커널을 사용하는 GPR 을 보여줍니다.

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# RBF 커널과 WhiteKernel 을 사용하여 GPR 모델 생성
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# 학습 데이터에 모델 적합
model.fit(X_train, y_train)

# 학습된 모델을 사용하여 예측
y_pred = model.predict(X_test)
```

GPR 과 커널 릿지 회귀 비교: 커널 릿지 회귀 (KRR) 와 GPR 모두 "커널 트릭"을 사용하여 대상 함수를 학습합니다. GPR 은 생성적 확률 모델을 학습하고 신뢰 구간을 제공할 수 있지만, KRR 은 예측만 제공합니다.

```python
from sklearn.kernel_ridge import KernelRidge

# 커널 릿지 회귀 모델 생성
krr_model = KernelRidge(kernel='rbf')

# 학습 데이터에 KRR 모델 적합
krr_model.fit(X_train, y_train)

# KRR 모델을 사용하여 예측
krr_y_pred = krr_model.predict(X_test)

# GPR 결과와 비교
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

마우나 로아 CO2 데이터에 대한 GPR: 이 예제는 로그 - 주변 - 가능도에 대한 기울기 상승을 사용하여 복잡한 커널 엔지니어링과 하이퍼파라미터 최적화를 보여줍니다. 이 데이터는 하와이 마우나 로아 천문대에서 수집된 월별 평균 대기 CO2 농도로 구성됩니다. 목표는 시간의 함수로서 CO2 농도를 모델링하는 것입니다.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# 구성된 커널을 사용하여 GPR 모델 생성
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# 데이터에 모델 적합
model.fit(X_train, y_train)

# 학습된 모델을 사용하여 예측
y_pred = model.predict(X_test)
```
