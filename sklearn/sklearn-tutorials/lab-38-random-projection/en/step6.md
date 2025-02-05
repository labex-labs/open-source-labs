# Verification

To verify the correctness of the inverse transform, we can compare the original data `X` with the result of the inverse transform.

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

Here, we apply the transform to the inverse transformed data `X_new_inversed` and check if it is equal to the original projected data `X_new` using the `np.allclose` function.
