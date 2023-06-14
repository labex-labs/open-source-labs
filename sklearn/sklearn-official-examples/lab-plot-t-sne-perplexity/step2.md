# Create Data

We will create three different datasets to illustrate the use of t-SNE. The first dataset will be two concentric circles.

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```


