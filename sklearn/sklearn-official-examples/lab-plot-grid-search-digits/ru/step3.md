# Определение гиперпараметров

Мы определим гиперпараметры и создадим экземпляр `GridSearchCV`.

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
