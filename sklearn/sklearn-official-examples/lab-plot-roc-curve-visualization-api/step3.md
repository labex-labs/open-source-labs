# Train a Random Forest and Plot the ROC Curve

In this step, we will train a random forest classifier and plot its ROC curve alongside the SVC ROC curve. To do this, we will create a new `RandomForestClassifier` object, fit it to the training data, and then create a new `RocCurveDisplay` object using this classifier. We will also pass the `ax` parameter to this function to plot the curves on the same axis. Finally, we will call the `plot()` method of the `svc_disp` object to plot the SVC ROC curve.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
