# Load the yeast dataset

```python
X, Y = fetch_openml("yeast", version=4, return_X_y=True, parser="pandas")
Y = Y == "TRUE"
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
```
