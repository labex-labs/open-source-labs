# Distance Metrics

Distance metrics are functions that measure the dissimilarity between two objects. These metrics satisfy certain conditions, such as non-negativity, symmetry, and the triangle inequality.

Some popular distance metrics include Euclidean distance, Manhattan distance, and Minkowski distance.

Let's calculate the pairwise distances between two sets of samples using the `pairwise_distances` function:

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise distances between X and Y
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

Output:

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
