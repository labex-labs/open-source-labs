# データセット

100,000 個のサンプルと 20 個の特徴量を持つ合成二値分類データセットを使用します。20 個の特徴量のうち、情報的なものは 2 個だけで、10 個は冗長（情報的な特徴量のランダムな組み合わせ）で、残りの 8 個は非情報的（ランダムな数）です。100,000 個のサンプルのうち、1,000 個はモデルのフィッティングに使用され、残りはテストに使用されます。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```
