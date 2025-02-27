# Загрузка датасета Titanic

Далее мы загрузим датасет Titanic, чтобы продемонстрировать `set_output` с использованием `compose.ColumnTransformer` и неоднородных данных.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```
