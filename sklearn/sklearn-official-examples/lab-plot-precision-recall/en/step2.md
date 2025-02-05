# Plot the Precision-Recall Curve

To plot the Precision-Recall curve, we will use the PrecisionRecallDisplay class from the sklearn.metrics library. We can use either from_estimator or from_predictions method to compute the curve. The from_estimator method computes the predictions for us before plotting the curve, while the from_predictions method requires us to provide the predicted scores.

```python
from sklearn.metrics import PrecisionRecallDisplay

# Using from_estimator method
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")

# Using from_predictions method
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")
```
