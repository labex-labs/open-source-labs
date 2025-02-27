# アウトライア予測関数

次のステップは、アウトライア予測関数を定義することです。この例では、`LocalOutlierFactor` と `IsolationForest` アルゴリズムを使用します。`compute_prediction` 関数は、Xの平均アウトライアスコアを返します。

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"{model_name} の予測を計算中...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
