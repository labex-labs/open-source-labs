# Загрузка датасета

В этом шаге мы загрузим датасет Titanic из OpenML с использованием `fetch_openml`.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
