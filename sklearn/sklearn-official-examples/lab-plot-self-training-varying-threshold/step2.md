# Load Data

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

The `breast_cancer` dataset is loaded and shuffled. We then copy the true labels to `y_true`, and remove all labels except for the first 50 samples from `y`. This will be used to simulate a semi-supervised learning scenario.


