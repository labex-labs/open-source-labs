# Import Libraries and Generate Dataset

We start by importing the necessary libraries and generating a synthetic binary classification dataset with 100,000 samples and 20 features. Of the 20 features, only 2 are informative, 2 are redundant, and the remaining 16 are uninformative. Of the 100,000 samples, 100 will be used for model fitting and the remaining for testing.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dataset
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Samples used for training the models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```


