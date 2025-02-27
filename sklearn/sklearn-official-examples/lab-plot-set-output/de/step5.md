# Lade den Titanic-Datensatz

Als nächstes laden wir den Titanic-Datensatz, um `set_output` mit `compose.ColumnTransformer` und heterogenen Daten zu demonstrieren.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```
