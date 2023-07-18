# Load or generate small datasets

Now, we need to load or generate the small datasets we will use for this example. We will use the iris dataset, the digits dataset, and two datasets generated using make_circles and make_moons functions.

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```
