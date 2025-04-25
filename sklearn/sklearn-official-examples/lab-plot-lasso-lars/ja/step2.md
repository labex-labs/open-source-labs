# Lasso パスの計算

次に、LARS アルゴリズムを使用して Lasso パスを計算します。Scikit-Learn の`linear_model`モジュールの`lars_path`関数を使用して Lasso パスを計算します。この関数は、入力特徴、目的変数、およびメソッドをパラメータとして受け取ります。この場合、L1 正則化には「lasso」メソッドを使用します。

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
