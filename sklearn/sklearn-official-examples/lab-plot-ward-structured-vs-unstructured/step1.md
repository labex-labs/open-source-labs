# Generate Data

We start by generating the Swiss Roll dataset using the `make_swiss_roll` function from Scikit-learn. The Swiss Roll dataset is a 3D dataset with a spiral shape.

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# Make it thinner
X[:, 1] *= 0.5
```
