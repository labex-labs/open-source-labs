# Generate Swiss Roll Dataset

We start by generating the Swiss Roll dataset using the `make_swiss_roll()` function from `sklearn.datasets`. This function generates a 3D dataset with a spiral shape.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```


