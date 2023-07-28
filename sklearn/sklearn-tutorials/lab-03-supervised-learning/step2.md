# Linear Regression

In this step, we will explore the concept of linear regression and how it can be implemented using scikit-learn. We will use the diabetes dataset, which consists of physiological variables of patients and their disease progression after one year.

#### Load the Diabetes Dataset

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### Create and Fit a Linear Regression Model

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### Make Predictions and Calculate Performance Metrics

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
