# Retrieve dataframes from OpenML

fetch_openml can now return pandas dataframe and thus properly handle datasets with heterogeneous data.

```python
from sklearn.datasets import fetch_openml

titanic = fetch_openml("titanic", version=1, as_frame=True, parser="pandas")
print(titanic.data.head()[["pclass", "embarked"]])
```
