# Computing Principal Singular Vector using Randomized SVD

We will compute the principal singular vectors using the randomized_svd method implemented in scikit-learn.

```python
from sklearn.decomposition import randomized_svd

print("Computing the principal singular vectors using randomized_svd")
U, s, V = randomized_svd(X, 5, n_iter=3)
```


