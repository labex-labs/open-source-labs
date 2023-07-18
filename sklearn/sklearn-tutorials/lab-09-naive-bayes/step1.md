# Import Libraries and Load the Dataset

Let's start by importing the necessary libraries and loading the iris dataset. We will use the `load_iris` function from the `sklearn.datasets` module to load the dataset.

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target variable

print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of classes:", len(set(y)))
```
