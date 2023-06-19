# Create the RFE Object and Fit the Data

Next, we will create an object of the RFE class and fit the data to it. We will use a Support Vector Classifier (SVC) with a linear kernel as the estimator. We will select one feature at a time and take one step at a time.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```


