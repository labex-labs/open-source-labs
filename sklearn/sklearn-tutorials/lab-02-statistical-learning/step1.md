# Understanding Datasets

Scikit-learn represents datasets as 2D arrays, where the first axis represents the samples and the second axis represents the features. Let's take a look at an example using the iris dataset:

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

Output:

```
(150, 4)
```

The iris dataset consists of 150 observations of irises, with each observation described by 4 features. The shape of the data array is (150, 4).
