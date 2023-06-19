# Predict

In this step, we will make predictions using the models we created in the previous step. We will use `np.arange` to create a new array of values from -100 to 100 with an interval of 0.01, and then use `predict` method from our models to predict the output.

```python
# Predict
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```


