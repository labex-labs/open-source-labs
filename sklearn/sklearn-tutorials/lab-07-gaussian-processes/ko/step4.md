# GPC 예제

GPC 를 이용한 확률적 예측: 이 예제는 서로 다른 하이퍼파라미터 선택에 따른 GPC 의 예측 확률을 보여줍니다.

```python
# RBF 커널을 사용하여 GPC 모델 생성
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 학습 데이터에 모델 적합
model.fit(X_train, y_train)

# 테스트 데이터의 클래스 확률 예측
y_prob = model.predict_proba(X_test)
```

XOR 데이터셋에서의 GPC 예시: 이 예제는 XOR 데이터셋에서 GPC 를 사용하는 방법을 보여줍니다. 정상 동방성 커널 (RBF) 과 비정상 동방성 커널 (DotProduct) 을 사용한 결과를 비교합니다.

```python
# 서로 다른 커널을 사용하여 GPC 모델 생성
isotropic_kernel = RBF(length_scale=1.0)
non_stationary_kernel = DotProduct(sigma_0=1.0)

# XOR 데이터셋에 모델 적합
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
non_stationary_model = GaussianProcessClassifier(kernel=non_stationary_kernel)
isotropic_model.fit(X_xor, y_xor)
non_stationary_model.fit(X_xor, y_xor)

# 학습된 모델을 사용하여 예측
isotropic_y_pred = isotropic_model.predict(X_test)
non_stationary_y_pred = non_stationary_model.predict(X_test)
```

붓꽃 데이터셋에서의 GPC: 이 예제는 등방성 RBF 커널과 이방성 RBF 커널을 사용하여 붓꽃 데이터셋에서 GPC 를 보여줍니다. 서로 다른 하이퍼파라미터 선택이 예측 확률에 미치는 영향을 보여줍니다.

```python
# 서로 다른 커널을 사용하여 GPC 모델 생성하고 붓꽃 데이터셋에 적합
isotropic_kernel = RBF(length_scale=1.0)
anisotropic_kernel = RBF(length_scale=[1.0, 2.0])
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
anisotropic_model = GaussianProcessClassifier(kernel=anisotropic_kernel)
isotropic_model.fit(X_train, y_train)
anisotropic_model.fit(X_train, y_train)

# 클래스 확률 예측
isotropic_y_prob = isotropic_model.predict_proba(X_test)
anisotropic_y_prob = anisotropic_model.predict_proba(X_test)
```
