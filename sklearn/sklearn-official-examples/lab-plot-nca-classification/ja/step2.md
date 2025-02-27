# データの読み込みと準備

次に、データを読み込んで準備します。scikit-learnを使ってアイリスデータセットを読み込み、2つの特徴量のみを選択します。その後、データを訓練セットとテストセットに分割します。

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# we only take two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
