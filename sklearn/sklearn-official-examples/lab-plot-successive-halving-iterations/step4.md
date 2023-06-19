# Creating a Halving Random Search Object

Create a `HalvingRandomSearchCV` object to search through the parameter space. The object takes the following arguments:

- `estimator`: the estimator to be optimized
- `param_distributions`: the parameter space to search through
- `factor`: the factor by which the number of candidates is reduced in each iteration
- `random_state`: the random state used for the search

The code to create the object is as follows:

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```


