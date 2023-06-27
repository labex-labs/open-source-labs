# Define the Model

We use a support vector classifier with a radial basis function kernel.

```python
from sklearn.svm import SVC

# We will use a Support Vector Classifier with "rbf" kernel
svm = SVC(kernel="rbf")
```
