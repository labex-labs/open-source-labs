# Carregar o conjunto de dados Titanic

Em seguida, carregaremos o conjunto de dados Titanic para demonstrar `set_output` com `compose.ColumnTransformer` e dados heterogêneos.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```
