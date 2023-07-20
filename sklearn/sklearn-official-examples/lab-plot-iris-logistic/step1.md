# Load the Dataset and Preprocess

We will use scikit-learn library to load the Iris dataset. The dataset contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Each instance has 4 features: sepal length, sepal width, petal length, and petal width.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target
```
