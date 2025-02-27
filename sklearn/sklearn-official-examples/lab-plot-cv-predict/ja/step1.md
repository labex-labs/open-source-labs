# データの読み込みと準備

まず、糖尿病データセットを読み込み、モデリングのために準備します。scikit-learn の `load_diabetes` 関数を使って、データセットを 2 つの配列 `X` と `y` に読み込みます。

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
