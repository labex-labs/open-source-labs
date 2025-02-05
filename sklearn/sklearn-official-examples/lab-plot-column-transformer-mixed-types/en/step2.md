# Load the Dataset

In this step, we will load the Titanic dataset from OpenML using `fetch_openml`.

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
