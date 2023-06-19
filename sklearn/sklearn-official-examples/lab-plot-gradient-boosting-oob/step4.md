# Compute Best Number of Iterations for Test Data

We can also compute the best number of iterations for the test data. We will compute the negative log-loss for each number of iterations on the test data.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```


