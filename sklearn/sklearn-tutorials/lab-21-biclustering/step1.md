# Import necessary libraries and dataset

First, let's import the necessary libraries and load a sample dataset that we will use for biclustering.

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Load sample data
data = np.arange(100).reshape(10, 10)
```
