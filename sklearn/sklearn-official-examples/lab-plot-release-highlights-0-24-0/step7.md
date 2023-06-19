# Individual Conditional Expectation Plots

A new kind of partial dependence plot is available: the Individual Conditional Expectation (ICE) plot. ICE plots visualize the dependence of the prediction on a feature for each sample separately, with one line per sample.

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.inspection import PartialDependenceDisplay

# load the california housing dataset
X, y = fetch_california_housing(return_X_y=True, as_frame=True)
features = ["MedInc", "AveOccup", "HouseAge", "AveRooms"]

# create the classifier
est = RandomForestRegressor(n_estimators=10)
est.fit(X, y)

# plot the ICE plot
display = PartialDependenceDisplay.from_estimator(
    est,
    X,
    features,
    kind="individual",
    subsample=50,
    n_jobs=3,
    grid_resolution=20,
    random_state=0,
)
display.figure_.suptitle(
    "Partial dependence of house value on non-location features\n"
    "for the California housing dataset, with BayesianRidge"
)
display.figure_.subplots_adjust(hspace=0.3)
```


