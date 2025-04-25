# データセットを読み込む

`sklearn.datasets` の `make_circles` 関数を使って、2 つの入れ子になった円から構成されるデータセットを作成します。

```python
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
