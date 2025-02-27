# 密集データの生成

次に、Lasso回帰に使用する密集データを生成します。Scikit-learnの`make_regression`関数を使って、5000個の特徴量を持つ200個のサンプルを生成します。

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
