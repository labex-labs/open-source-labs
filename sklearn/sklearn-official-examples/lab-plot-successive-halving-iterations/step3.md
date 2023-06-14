# Defining the Parameter Space

Define a dictionary `param_dist` that contains the hyperparameters and their respective values to search through. The hyperparameters are `max_depth`, `max_features`, `min_samples_split`, `bootstrap`, and `criterion`. The search range for `max_features` and `min_samples_split` is defined using the `randint` function from the `scipy.stats` module. The code to define the parameter space is as follows:

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```


