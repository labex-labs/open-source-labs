# Load the Data

We will use the breast cancer dataset from scikit-learn. This dataset has 30 features and a binary target variable indicating if a patient has malignant or benign cancer.

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
