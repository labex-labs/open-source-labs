# Carregar o Conjunto de Dados

Neste passo, carregaremos o conjunto de dados Titanic do OpenML utilizando `fetch_openml`.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
