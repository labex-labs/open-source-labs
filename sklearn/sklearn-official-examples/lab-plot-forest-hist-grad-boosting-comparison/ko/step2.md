# 모델 및 매개변수 그리드 정의

scikit-learn 의 `RandomForestRegressor`, `HistGradientBoostingRegressor`, 및 `GridSearchCV` 클래스를 사용하여 랜덤 포레스트와 히스토그램 기반 그래디언트 부스팅 두 가지 모델과 해당 매개변수 그리드를 정의합니다. 또한 병렬 처리에 사용할 호스트 머신의 물리적 코어 수를 설정합니다.

```python
import joblib
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import GridSearchCV, KFold

N_CORES = joblib.cpu_count(only_physical_cores=True)

models = {
    "Random Forest": RandomForestRegressor(
        min_samples_leaf=5, random_state=0, n_jobs=N_CORES
    ),
    "Hist Gradient Boosting": HistGradientBoostingRegressor(
        max_leaf_nodes=15, random_state=0, early_stopping=False
    ),
}

param_grids = {
    "Random Forest": {"n_estimators": [10, 20, 50, 100]},
    "Hist Gradient Boosting": {"max_iter": [10, 20, 50, 100, 300, 500]},
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
