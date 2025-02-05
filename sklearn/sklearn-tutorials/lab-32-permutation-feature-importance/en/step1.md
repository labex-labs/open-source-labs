# Load the dataset

First, we need to load a dataset that we can use to train our predictive model. We will use the Diabetes dataset from scikit-learn, which contains information about diabetes patients.

```python
from sklearn.datasets import load_diabetes

# Load the Diabetes dataset
diabetes = load_diabetes()

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```
