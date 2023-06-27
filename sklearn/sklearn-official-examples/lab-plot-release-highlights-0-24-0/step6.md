# New PolynomialCountSketch Kernel Approximation Function

The new `PolynomialCountSketch` approximates a polynomial expansion of a feature space when used with linear models, but uses much less memory than `PolynomialFeatures`.

```python
from sklearn.datasets import fetch_covtype
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.kernel_approximation import PolynomialCountSketch
from sklearn.linear_model import LogisticRegression

# load the covtype dataset
X, y = fetch_covtype(return_X_y=True)

# create the pipeline
pipe = make_pipeline(
    MinMaxScaler(),
    PolynomialCountSketch(degree=2, n_components=300),
    LogisticRegression(max_iter=1000),
)

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# fit the model
pipe.fit(X_train, y_train).score(X_test, y_test)
```
