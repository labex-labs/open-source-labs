# 密集データの生成

次に、Lasso 回帰に使用する密集データを生成します。Scikit-learn の`make_regression`関数を使って、5000 個の特徴量を持つ 200 個のサンプルを生成します。

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
