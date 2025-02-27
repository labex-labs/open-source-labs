# データセットの生成と分割

まず、Scikit-learn の `make_classification` 関数を使って二値分類用のデータセットを生成します。また、Scikit-learn の `train_test_split` 関数を使って、データセットを訓練用とテスト用のサブセットに分割します。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```
