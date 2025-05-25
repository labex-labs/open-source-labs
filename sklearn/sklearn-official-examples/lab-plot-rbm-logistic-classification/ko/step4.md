# 평가

이 단계에서는 테스트 데이터 세트에 대한 모델의 성능을 평가합니다. `sklearn.metrics` 모듈의 `classification_report` 함수를 사용하여 파이프라인 모델과 로지스틱 회귀 모델 모두에 대한 분류 보고서를 생성합니다.

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "RBM 특징을 사용한 로지스틱 회귀:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# 픽셀 데이터 자체로 로지스틱 회귀 분류기를 직접 훈련
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "원본 픽셀 특징을 사용한 로지스틱 회귀:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
