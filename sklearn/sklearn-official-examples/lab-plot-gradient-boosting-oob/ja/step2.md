# OOB 推定を備えた分類器を適合させる

次に、`sklearn.ensemble` モジュールの `GradientBoostingClassifier` クラスを使用して、OOB 推定を備えた勾配ブースティング分類器を作成します。推定器の数を 100 に設定し、学習率を 0.1 に設定します。

```python
from sklearn.ensemble import GradientBoostingClassifier

params = {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "subsample": 1.0,
    "max_depth": 3,
    "min_samples_leaf": 1,
    "random_state": 1,
    "oob_score": True
}

clf = GradientBoostingClassifier(**params)
clf.fit(X, y)
```
