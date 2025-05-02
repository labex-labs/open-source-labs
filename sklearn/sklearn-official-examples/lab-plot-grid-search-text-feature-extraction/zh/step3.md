# 超参数调整

我们使用随机搜索交叉验证（RandomizedSearchCV）来探索超参数网格，并为管道找到最佳的超参数组合。在这种情况下，我们设置 `n_iter=40` 以限制搜索空间。我们可以增加 `n_iter` 以获得更全面的分析，但这会增加计算时间。

```python
from pprint import pprint
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
