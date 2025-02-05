# Loading the Data

We load the Diabetes dataset from scikit-learn and print its description.

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
