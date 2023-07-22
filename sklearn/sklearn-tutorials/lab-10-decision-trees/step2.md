# Load the Dataset

Next, we will load the Iris dataset. This dataset contains information about four features of three different species of Iris flowers. We will use this dataset to train our Decision Tree classifier.

```python
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
```
