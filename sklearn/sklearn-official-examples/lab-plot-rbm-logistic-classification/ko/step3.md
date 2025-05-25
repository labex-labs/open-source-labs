# 훈련

이 단계에서는 이전 단계에서 정의된 파이프라인 모델을 훈련합니다. 모델의 하이퍼파라미터 (학습률, 은닉층 크기, 정규화) 를 설정하고 훈련 데이터를 모델에 맞춥니다.

```python
from sklearn.base import clone

# 하이퍼파라미터. 이 값들은 교차 검증 (cross-validation) 을 통해 설정되었습니다.
# 여기서는 시간 절약을 위해 교차 검증을 수행하지 않습니다.
rbm.learning_rate = 0.06
rbm.n_iter = 10

# 더 많은 구성 요소는 일반적으로 더 나은 예측 성능을 제공하지만, 훈련 시간이 더 길어집니다.
rbm.n_components = 100
logistic.C = 6000

# RBM-로지스틱 파이프라인 훈련
rbm_features_classifier.fit(X_train, Y_train)
```
