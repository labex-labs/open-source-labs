# ライブラリのインポートとデータセットの生成

必要なライブラリをインポートし、100,000 個のサンプルと 20 個の特徴を持つ合成バイナリ分類データセットを生成します。20 個の特徴のうち、情報的なものは 2 個、冗長なものは 2 個、その他の 16 個は情報のないものです。100,000 個のサンプルのうち、100 個はモデルのフィッティングに使用され、残りはテストに使用されます。

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dataset
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Samples used for training the models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```
