# Define a function to get initial means

Next, we will define a function `get_initial_means` that takes the sample data, initialization method, and random state as inputs and returns the initialization means.

```python
def get_initial_means(X, init_params, r):
    # Run a GaussianMixture with max_iter=0 to output the initialization means
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
