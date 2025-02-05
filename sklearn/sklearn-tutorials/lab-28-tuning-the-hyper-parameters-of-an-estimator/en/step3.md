# Define the estimator and parameter grid

Now we need to define the estimator that we want to tune and the parameter grid that we want to search. The parameter grid specifies the values that we want to try for each hyperparameter.

```python
from sklearn.svm import SVC

# Create an instance of the support vector classifier
svc = SVC()

# Define the parameter grid
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```
