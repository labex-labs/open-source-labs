# Load and Prepare the Data

Next, we will load and prepare the data. We will load the Iris dataset using scikit-learn and select only two features. We will then split the data into a training set and a testing set.

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# we only take two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
