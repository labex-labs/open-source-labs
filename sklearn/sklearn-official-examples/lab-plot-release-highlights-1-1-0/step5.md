# MiniBatchNMF

The new class `MiniBatchNMF` implements a faster but less accurate version of non-negative matrix factorization (`NMF`). `MiniBatchNMF` divides the data into mini-batches and optimizes the NMF model in an online manner by cycling over the mini-batches, making it better suited for large datasets. In particular, it implements `partial_fit`, which can be used for online learning when the data is not readily available from the start, or when the data does not fit into memory.

```python
import numpy as np
from sklearn.decomposition import MiniBatchNMF

rng = np.random.RandomState(0)
n_samples, n_features, n_components = 10, 10, 5
true_W = rng.uniform(size=(n_samples, n_components))
true_H = rng.uniform(size=(n_components, n_features))
X = true_W @ true_H

nmf = MiniBatchNMF(n_components=n_components, random_state=0)

for _ in range(10):
    nmf.partial_fit(X)

W = nmf.transform(X)
H = nmf.components_
X_reconstructed = W @ H

print(
    f"relative reconstruction error: ",
    f"{np.sum((X - X_reconstructed) ** 2) / np.sum(X**2):.5f}",
)
```


