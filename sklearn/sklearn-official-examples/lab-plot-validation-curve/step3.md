# Computing Validation Scores

We will use the `validation_curve` function from scikit-learn to compute the training and validation scores for the SVM classifier with different values of gamma.

```python
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

train_scores, test_scores = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    scoring="accuracy",
    n_jobs=2,
)
```
