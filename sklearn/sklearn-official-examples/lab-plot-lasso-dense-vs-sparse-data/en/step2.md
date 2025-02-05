# Generate Dense Data

Next, we generate some dense data that we will use for the Lasso regression. We use Scikit-learn's `make_regression` function to generate 200 samples with 5000 features.

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
