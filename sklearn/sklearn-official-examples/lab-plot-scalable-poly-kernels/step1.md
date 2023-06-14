# Load and Prepare the Data

We will first load the Covtype dataset and transform it into a binary classification problem by selecting only one class. Then, we will partition the data into a training set and a testing set, and normalize the features.

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# Load the Covtype dataset, selecting only one class
X, y = fetch_covtype(return_X_y=True)
y[y != 2] = 0
y[y == 2] = 1

# Partition the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# Normalize the features
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```


