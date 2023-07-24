# Create sample dataset

We will create a sample dataset using numpy library. We will create six datasets with different standard deviations.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```
