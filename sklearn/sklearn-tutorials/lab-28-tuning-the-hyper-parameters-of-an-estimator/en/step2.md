# Load the dataset

Next, let's load the dataset that we will be working with. We can use any dataset of our choice for this exercise.

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Split the data into features and target
X = iris.data
y = iris.target
```
