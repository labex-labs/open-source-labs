# 모델 정의

이 단계에서는 베르누이 RBM 특징 추출기와 로지스틱 회귀 분류기를 사용하여 분류 파이프라인을 정의합니다. `sklearn.neural_network` 모듈의 `BernoulliRBM` 클래스와 `sklearn.linear_model` 모듈의 `LogisticRegression` 클래스를 사용합니다. 그런 다음 두 모델을 결합하기 위해 파이프라인 객체 `rbm_features_classifier`를 생성합니다.

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```
