# 검증 점수 계산

다양한 감마 값을 사용하여 SVM 분류기의 학습 및 검증 점수를 계산하기 위해 scikit-learn 의 `validation_curve` 함수를 사용합니다.

```python
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

train_scores, test_scores = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    scoring="accuracy",
    n_jobs=2,
)
```
