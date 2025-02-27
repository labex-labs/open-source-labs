# データセット

100,000個のサンプルと20個の特徴量を持つ合成二値分類データセットを使用します。20個の特徴量のうち、情報的なものは2個だけで、10個は冗長（情報的な特徴量のランダムな組み合わせ）で、残りの8個は非情報的（ランダムな数）です。100,000個のサンプルのうち、1,000個はモデルのフィッティングに使用され、残りはテストに使用されます。

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
