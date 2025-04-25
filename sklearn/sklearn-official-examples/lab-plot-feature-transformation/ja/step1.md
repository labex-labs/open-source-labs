# データの準備

まず、80,000 サンプルの大きなデータセットを作成し、それを 3 つのセットに分割します。

- 後で特徴量エンジニアリングの変換器として使用されるアンサンブル手法を学習するためのセット
- 線形モデルを学習するためのセット
- 線形モデルをテストするためのセット。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```
