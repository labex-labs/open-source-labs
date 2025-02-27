# Lade den Datensatz

In diesem Schritt laden wir den Titanic-Datensatz von OpenML mit `fetch_openml`.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
