# モデルとパラメータグリッドの定義

scikit-learnの`RandomForestRegressor`、`HistGradientBoostingRegressor`、および`GridSearchCV`クラスを使って、ランダムフォレストとヒストグラム勾配ブースティングの2つのモデルとそれに対応するパラメータグリッドを定義します。また、並列処理に使用するホストマシン上の物理コア数も設定します。

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
