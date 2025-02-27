# モデルの学習と選択

コンポーネント数を 1 から 6 まで変化させ、使用する共分散パラメータの種類を以下のように変えます。

- `"full"`：各コンポーネントが独自の一般的な共分散行列を持つ。
- `"tied"`：すべてのコンポーネントが同じ一般的な共分散行列を共有する。
- `"diag"`：各コンポーネントが独自の対角共分散行列を持つ。
- `"spherical"`：各コンポーネントが独自の単一分散を持つ。

異なるモデルを評価し、最適なモデル（最も低い BIC）を選択します。これは、`GridSearchCV` とユーザ定義のスコア関数を使用して行われ、負の BIC スコアを返します。最適なパラメータセットと推定器は、それぞれ `best_parameters_` と `best_estimator_` に格納されます。

```python
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV

def gmm_bic_score(estimator, X):
    """Callable to pass to GridSearchCV that will use the BIC score."""
    # Make it negative since GridSearchCV expects a score to maximize
    return -estimator.bic(X)

param_grid = {
    "n_components": range(1, 7),
    "covariance_type": ["spherical", "tied", "diag", "full"],
}
grid_search = GridSearchCV(
    GaussianMixture(), param_grid=param_grid, scoring=gmm_bic_score
)
grid_search.fit(X)
```
