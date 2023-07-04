# Score and Cross-Validated Scores

Estimators in scikit-learn expose a `score` method that can be used to assess the quality of the model's fit or prediction on new data. This method returns a score, where a higher value indicates better performance.

```python
from sklearn import datasets, svm

# Load the digits dataset
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# Create an SVM classifier with linear kernel
svc = svm.SVC(C=1, kernel='linear')

# Fit the classifier on the training data and calculate the score on the test data
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

To get a better measure of prediction accuracy, we can use cross-validation. Cross-validation involves splitting the data into multiple folds, using each fold as a test set and the remaining folds as training sets. This process is repeated multiple times, and the scores are averaged to get the overall performance.

```python
import numpy as np

# Split the data into 3 folds
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# Perform cross-validation
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
