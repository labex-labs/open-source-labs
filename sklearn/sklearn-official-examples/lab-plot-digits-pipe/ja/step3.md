# データセットを読み込み、GridSearchCV のパラメータを定義する

digits データセットを読み込み、GridSearchCV のパラメータを定義します。PCA トランケーションと分類器の正則化のパラメータを設定します。

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```
