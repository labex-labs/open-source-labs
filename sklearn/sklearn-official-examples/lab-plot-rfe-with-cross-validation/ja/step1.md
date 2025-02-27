# データ生成

scikit-learnの`make_classification`関数を使って分類タスクを生成します。15個の特徴を持つ500個のサンプルを生成します。そのうち3個は情報的で、2個は冗長で、10個は非情報的です。

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=15,
    n_informative=3,
    n_redundant=2,
    n_repeated=0,
    n_classes=8,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=0,
)
```
