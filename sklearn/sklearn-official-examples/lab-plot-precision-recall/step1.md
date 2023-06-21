# Dataset and Model

We will use the iris dataset and a Linear SVC classifier to differentiate two types of irises. First, we will import the necessary libraries and load the dataset.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

Next, we will add noisy features to the dataset and split it into training and test sets.

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

Finally, we will scale the data using a StandardScaler and fit a Linear SVC classifier to the training data.

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
