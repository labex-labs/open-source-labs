# Hyperparameter Tuning

We use RandomizedSearchCV to explore the grid of hyperparameters and find the best combination of hyperparameters for the pipeline. In this case, we set n_iter=40 to limit the search space. We can increase n_iter to get a more informative analysis, but it will increase the computation time.

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Performing grid search...")
print("Hyperparameters to be evaluated:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)

```


