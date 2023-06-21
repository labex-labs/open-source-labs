# Prepare the Data

In this step, we will prepare the synthetic classification datasets for feature discretization. We will use the scikit-learn library to generate three different datasets: moons, concentric circles, and linearly separable data.

```python
h = 0.02  # step size in the mesh

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
