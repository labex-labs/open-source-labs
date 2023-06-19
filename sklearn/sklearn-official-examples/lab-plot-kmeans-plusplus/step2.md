# Calculate seeds from k-means++

We will use the scikit-learn library's `kmeans_plusplus` function to calculate seeds from k-means++. This function returns the initial cluster centers that are used for k-means clustering. We will calculate 4 clusters using k-means++.

```python
# Calculate seeds from k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```


