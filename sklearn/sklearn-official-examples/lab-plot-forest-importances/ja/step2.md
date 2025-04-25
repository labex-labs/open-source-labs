# データの生成

3 つの情報量のある特徴量のみからなる合成データセットを生成します。データセットをシャッフルしないように明示的に設定し、情報量のある特徴量が X の最初の 3 列に対応するようにします。また、データセットを学習用とテスト用のサブセットに分割します。

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
