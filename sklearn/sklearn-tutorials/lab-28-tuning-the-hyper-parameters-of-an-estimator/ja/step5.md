# 交差検証を用いたランダムサーチを実行する

ランダムサーチは、パラメータグリッドのサブセットをランダムにサンプリングし、交差検証を使用して各組み合わせの性能を評価します。パラメータ空間が大きく、網羅的な検索が実行不可能な場合に便利です。

```python
# Create an instance of RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Fit the data to perform randomized search
random_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', random_search.best_params_)
```
