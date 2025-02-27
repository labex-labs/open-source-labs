# ハイパーパラメータ最適化のためのランダムサーチ

ランダムサーチを使ってハイパーパラメータ空間を探索し、SVMモデルに最適なハイパーパラメータを見つけます。

```python
# specify parameters and distributions to sample from
param_dist = {
    "average": [True, False],
    "l1_ratio": stats.uniform(0, 1),
    "alpha": stats.loguniform(1e-2, 1e0),
}

# run randomized search
n_iter_search = 15
random_search = RandomizedSearchCV(
    clf, param_distributions=param_dist, n_iter=n_iter_search
)

start = time()
random_search.fit(X, y)
print(
    "RandomizedSearchCV took %.2f seconds for %d candidates parameter settings."
    % ((time() - start), n_iter_search)
)

# print results
report(random_search.cv_results_)
```
