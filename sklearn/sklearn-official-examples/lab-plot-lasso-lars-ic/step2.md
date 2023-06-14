# Preprocess the Data

We will scale the dataset using the StandardScaler method and fit the LassoLarsIC estimator with AIC criterion.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```


