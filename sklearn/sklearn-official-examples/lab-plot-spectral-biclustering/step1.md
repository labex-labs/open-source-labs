# Generate sample data

We generate the sample data using the `make_checkerboard` function. Each pixel within `shape=(300, 300)` represents with it's color a value from a uniform distribution. The noise is added from a normal distribution, where the value chosen for `noise` is the standard deviation.

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
_ = plt.show()
```


