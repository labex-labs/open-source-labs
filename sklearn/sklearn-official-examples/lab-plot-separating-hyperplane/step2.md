# Fit the SVM Model

Next, we will fit the SVM model to our dataset using a linear kernel and a regularization parameter of 1000. We will use the `svm.SVC()` function from scikit-learn to create the SVM classifier.

```python
from sklearn import svm

# fit the SVM model
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```


