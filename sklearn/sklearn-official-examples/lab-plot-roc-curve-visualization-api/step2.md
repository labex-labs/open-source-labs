# Plot the ROC Curve

Next, we will plot the ROC curve using the `RocCurveDisplay.from_estimator` function. This function takes the trained classifier, the test dataset, and the true labels as inputs, and returns an object that can be used to plot the ROC curve. We will then call the `show()` method to display the plot.

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```


