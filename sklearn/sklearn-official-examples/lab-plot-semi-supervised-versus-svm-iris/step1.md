# Load the Iris dataset and split the data

We will load the Iris dataset, which is a widely used dataset in machine learning for classification tasks. The dataset contains 150 samples of Iris flowers, with four features for each sample: sepal length, sepal width, petal length, and petal width. We will split the dataset into input features and target labels.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into input features and target labels
X = iris.data[:, :2] # We will only use the first two features for visualization purposes
y = iris.target
```
