# Set up the SVM classifier

We will set up an SVM classifier with a radial basis function (RBF) kernel. SVM is a supervised learning algorithm that finds the optimal hyperplane that separates the data into different classes.

```python
from sklearn.svm import SVC

# Set up the SVM classifier
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC with rbf kernel")
```
