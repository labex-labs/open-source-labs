# 合成データの生成

scikit-learn の `make_classification` 関数を使用して合成データを生成します。この関数は、n_informative 個の情報的な特徴、n_redundant 個の冗長な特徴、および各クラスに n_clusters_per_class 個のクラスターを持つランダムな n クラス分類問題を生成します。2 つの情報的な特徴と乱数シード 1 を使用して 1000 個のサンプルを生成します。その後、データを 60/40 の比率で訓練セットとテストセットに分割します。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
