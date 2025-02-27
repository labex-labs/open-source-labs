# モデルの学習

学習データを使ってIsolation Forestモデルを学習します。

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
