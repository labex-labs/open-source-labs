# ハイパーパラメータチューニング

RandomizedSearchCV を使用してハイパーパラメータのグリッドを探索し、パイプラインに最適なハイパーパラメータの組み合わせを見つけます。この場合、探索空間を制限するために `n_iter=40` を設定しています。`n_iter` を増やすとより詳細な分析が可能になりますが、計算時間が増加します。

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Performing grid search...")
print("Hyperparameters to be evaluated:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)

```
