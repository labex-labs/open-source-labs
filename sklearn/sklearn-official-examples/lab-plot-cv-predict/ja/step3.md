# 交差検証による予測の生成

scikit-learn の `cross_val_predict` 関数を使って、交差検証による予測を生成します。

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
