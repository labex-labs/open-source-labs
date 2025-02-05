# Establish a Baseline Model

We will train a linear SVM on the original features to establish a baseline model and print its accuracy.

```python
from sklearn.svm import LinearSVC

# Train a linear SVM on the original features
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# Print the accuracy of the baseline model
print(f"Linear SVM score on raw features: {lsvm_score:.2f}%")
```
