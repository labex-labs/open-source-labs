# Faster Parser in fetch_openml

`fetch_openml` now supports a new "pandas" parser that is more memory and CPU efficient. In v1.4, the default will change to parser="auto" which will automatically use the "pandas" parser for dense data and "liac-arff" for sparse data.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X.head()
```
