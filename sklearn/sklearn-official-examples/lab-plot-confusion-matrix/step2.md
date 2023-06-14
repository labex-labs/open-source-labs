# Load Data

We will use the iris dataset from scikit-learn. The dataset contains 150 samples, each with four features and a target label.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```


