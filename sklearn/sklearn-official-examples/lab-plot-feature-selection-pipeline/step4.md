# Evaluate the Pipeline

We will now evaluate the pipeline on the testing subset using the `predict` method. The pipeline will select the 3 most informative features based on the ANOVA F-value, and the `LinearSVC` function will make predictions on the selected features.

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```


