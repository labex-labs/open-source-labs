# Compare Coefficients of Dense Lasso and Sparse Lasso

We compare the coefficients of the dense Lasso model and the sparse Lasso model to ensure that they are producing the same results. We compute the Euclidean norm of the difference between the coefficients.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```
