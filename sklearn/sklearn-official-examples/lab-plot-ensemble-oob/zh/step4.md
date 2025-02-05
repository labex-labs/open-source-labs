# 计算袋外（OOB）错误率

对于每个分类器，我们将在一系列 `n_estimators` 值的范围内进行循环，并将分类器拟合到数据集上。我们会记录每个 `n_estimators` 值对应的 OOB 错误率，并将其存储在一个 `OrderedDict` 对象中。

```python
error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)

min_estimators = 15
max_estimators = 150

for label, clf in ensemble_clfs:
    for i in range(min_estimators, max_estimators + 1, 5):
        clf.set_params(n_estimators=i)
        clf.fit(X, y)

        oob_error = 1 - clf.oob_score_
        error_rate[label].append((i, oob_error))
```
