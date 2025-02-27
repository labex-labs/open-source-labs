# Определение моделей и сеток параметров

Мы определим две модели, Случайный лес и Градиентный бустинг с гистограммами, с соответствующими сетками параметров с использованием классов `RandomForestRegressor`, `HistGradientBoostingRegressor` и `GridSearchCV` из scikit-learn. Также мы установим количество физических ядер на хост-машине для параллельной обработки.

```python
import joblib
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import GridSearchCV, KFold

N_CORES = joblib.cpu_count(only_physical_cores=True)

models = {
    "Случайный лес": RandomForestRegressor(
        min_samples_leaf=5, random_state=0, n_jobs=N_CORES
    ),
    "Градиентный бустинг с гистограммами": HistGradientBoostingRegressor(
        max_leaf_nodes=15, random_state=0, early_stopping=False
    ),
}

param_grids = {
    "Случайный лес": {"n_estimators": [10, 20, 50, 100]},
    "Градиентный бустинг с гистограммами": {"max_iter": [10, 20, 50, 100, 300, 500]},
}

cv = KFold(n_splits=4, shuffle=True, random_state=0)

results = []

for name, model in models.items():
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grids[name],
        return_train_score=True,
        cv=cv,
    ).fit(X, y)

    result = {"model": name, "cv_results": pd.DataFrame(grid_search.cv_results_)}
    results.append(result)
```
