# Prepare the data

We will only take the first two features of the Iris dataset, which are the sepal length and sepal width. We will then split the data into the feature matrix `X` and the target vector `y`.

```python
X = iris.data[:, :2]
y = iris.target
```
