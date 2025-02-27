# ランダムなデータを生成する

scikit-learn の `make_regression` 関数を使ってランダムなデータを生成します。`n_samples` を 10、`n_features` を 10、`random_state` を 1 に設定します。この関数は、入力特徴量 X、目的変数 y、および真の係数値 w を返します。

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
