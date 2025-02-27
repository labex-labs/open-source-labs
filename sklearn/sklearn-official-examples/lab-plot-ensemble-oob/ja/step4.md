# OOBエラー率を計算する

各分類器に対して、`n_estimators`値の範囲をループして分類器をデータセットにフィットさせます。各`n_estimators`値に対するOOBエラー率を記録し、`OrderedDict`オブジェクトに格納します。

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
