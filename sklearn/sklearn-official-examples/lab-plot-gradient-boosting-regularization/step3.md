# Define Parameters

We will define the parameters for our Gradient Boosting Classifier. We will use the following parameters:

- n_estimators: number of boosting stages to perform
- max_leaf_nodes: maximum number of leaf nodes in each tree
- max_depth: maximum depth of the tree
- random_state: random seed for consistency
- min_samples_split: minimum number of samples required to split an internal node

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```
