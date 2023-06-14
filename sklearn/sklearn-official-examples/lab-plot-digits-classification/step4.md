# Split the Dataset

We will split the dataset into 50% train and 50% test subsets using `train_test_split()` method from `sklearn.model_selection`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```


