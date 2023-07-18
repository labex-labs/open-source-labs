# Univariate feature imputation using SimpleImputer

The `SimpleImputer` class provides basic strategies for imputing missing values in a univariate manner. We can choose from different strategies, such as replacing missing values with a constant value or using the mean, median, or most frequent value of each column to impute the missing values.

Let's start by considering the mean strategy. We will create an instance of `SimpleImputer` and fit it on our data to learn the imputation strategy. Then, we can use the `transform` method to impute the missing values based on the learned strategy.

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
