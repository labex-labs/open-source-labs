# Load Dataset and Define Parameters for GridSearchCV

We will load the digits dataset and define parameters for GridSearchCV. We will set the parameter for PCA truncation and classifier regularization.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```


