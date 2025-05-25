# 레이블 전파 모델 학습

이제 레이블이 지정된 데이터 포인트로 레이블 전파 모델을 학습하고, 나머지 레이블이 지정되지 않은 데이터 포인트의 레이블을 예측하는 데 사용합니다.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
