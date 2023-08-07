# Split the Data

We will split the data into training and test sets using the `train_test_split` function from scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
