# 모델 성능에 미치는 스케일링의 효과

PCA 로 차원 축소된 데이터를 사용하여 로지스틱 회귀 모델을 학습하고, 특징 스케일링이 모델 성능에 미치는 영향을 평가합니다. 스케일링된 특징과 스케일링되지 않은 특징을 사용한 모델의 성능을 비교합니다.

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss

Cs = np.logspace(-5, 5, 20)

unscaled_clf = make_pipeline(pca, LogisticRegressionCV(Cs=Cs))
unscaled_clf.fit(X_train, y_train)

scaled_clf = make_pipeline(scaler, pca, LogisticRegressionCV(Cs=Cs))
scaled_clf.fit(X_train, y_train)

y_pred = unscaled_clf.predict(X_test)
y_pred_scaled = scaled_clf.predict(X_test)
y_proba = unscaled_clf.predict_proba(X_test)
y_proba_scaled = scaled_clf.predict_proba(X_test)

print("스케일링되지 않은 PCA 에 대한 테스트 정확도")
print(f"{accuracy_score(y_test, y_pred):.2%}\n")
print("PCA 와 함께 표준화된 데이터에 대한 테스트 정확도")
print(f"{accuracy_score(y_test, y_pred_scaled):.2%}\n")
print("스케일링되지 않은 PCA 에 대한 로그 손실")
print(f"{log_loss(y_test, y_proba):.3}\n")
print("PCA 와 함께 표준화된 데이터에 대한 로그 손실")
print(f"{log_loss(y_test, y_proba_scaled):.3}")
```
