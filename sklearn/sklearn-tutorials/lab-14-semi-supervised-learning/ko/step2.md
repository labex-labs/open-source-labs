# 자기훈련 (Self Training)

#### 자기훈련 알고리즘 개요

자기훈련 알고리즘은 Yarowsky 의 알고리즘을 기반으로 합니다. 레이블이 지정되지 않은 데이터로부터 학습하여 지도 학습 분류기를 준지도 학습 분류기로 활용할 수 있도록 합니다. 이 알고리즘은 레이블이 지정된 데이터와 레이블이 지정되지 않은 데이터를 반복적으로 사용하여 지도 학습 분류기를 학습시키고, 레이블이 지정되지 않은 데이터에 대한 예측 결과를 사용하여 이러한 샘플의 일부를 레이블이 지정된 데이터에 추가합니다. 알고리즘은 모든 샘플에 레이블이 지정되거나 반복에서 새로운 샘플이 선택되지 않을 때까지 반복을 계속합니다.

#### scikit-learn 에서 자기훈련 사용

scikit-learn 에서 자기훈련 알고리즘은 `SelfTrainingClassifier` 클래스에 구현되어 있습니다. 이 알고리즘을 사용하려면 `predict_proba` 메서드를 구현하는 지도 학습 분류기를 제공해야 합니다. 자기훈련 알고리즘 사용 예시는 다음과 같습니다.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# 로지스틱 회귀 분류기를 생성합니다.
classifier = LogisticRegression()

# 로지스틱 회귀 분류기를 기본 분류기로 사용하는 자기훈련 분류기를 생성합니다.
self_training_classifier = SelfTrainingClassifier(classifier)

# 레이블이 지정된 데이터와 레이블이 지정되지 않은 데이터로 자기훈련 분류기를 학습시킵니다.
self_training_classifier.fit(X_labeled, y_labeled, X_unlabeled)

# 새로운 샘플에 대한 레이블을 예측합니다.
y_pred = self_training_classifier.predict(X_test)
```

위의 예에서 `X_labeled`와 `y_labeled`는 레이블이 지정된 데이터이고, `X_unlabeled`는 레이블이 지정되지 않은 데이터이며, `X_test`는 예측할 새로운 샘플입니다.
