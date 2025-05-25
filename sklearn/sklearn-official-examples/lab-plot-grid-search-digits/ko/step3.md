# 하이퍼파라미터 정의

하이퍼파라미터를 정의하고 `GridSearchCV` 인스턴스를 생성합니다.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

tuned_parameters = [
    {"kernel": ["rbf"], "gamma": [1e-3, 1e-4], "C": [1, 10, 100, 1000]},
    {"kernel": ["linear"], "C": [1, 10, 100, 1000]},
]

grid_search = GridSearchCV(
    SVC(), tuned_parameters, scoring=["precision", "recall"], refit=refit_strategy
)
```
