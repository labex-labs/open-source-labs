# Fit `SpectralBiclustering`

We fit the model and compare the obtained clusters with the ground truth. Note that when creating the model we specify the same number of clusters that we used to create the dataset (`n_clusters = (4, 3)`), which will contribute to obtain a good result.

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# Compute the similarity of two sets of biclusters
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"consensus score: {score:.1f}")
```


