# Charger le jeu de données

Dans cette étape, nous allons charger le jeu de données Titanic d'OpenML en utilisant `fetch_openml`.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
