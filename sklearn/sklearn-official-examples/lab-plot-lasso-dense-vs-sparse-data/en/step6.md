# Generate Sparse Data

Next, we generate some sparse data that we will use for the Lasso regression. We copy the dense data from the previous step and replace all values less than 2.5 with 0. We also convert the sparse data to Scipy's Compressed Sparse Column format.

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
