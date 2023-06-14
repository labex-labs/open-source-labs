# Log-loss Comparison

We compare the log loss of the uncalibrated and calibrated classifiers on the predictions of the 1000 test samples.

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("Log-loss of")
print(f" * uncalibrated classifier: {score:.3f}")
print(f" * calibrated classifier: {cal_score:.3f}")
```


