# Load Data

In this step, we will load the iris dataset using scikit-learn's datasets module. We will select the first two features of the dataset and assign it to the variable X. We will also assign the target variable to Y.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```


