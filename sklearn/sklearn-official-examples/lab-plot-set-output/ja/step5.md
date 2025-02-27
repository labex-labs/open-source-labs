# タイタニック号のデータセットを読み込む

次に、`compose.ColumnTransformer` と異種データを使った `set_output` を示すために、タイタニック号のデータセットを読み込みます。

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```
