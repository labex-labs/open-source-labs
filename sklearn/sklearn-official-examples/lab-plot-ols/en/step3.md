# Train the Model

Now, we create a linear regression object and train the model using the training sets.

```python
from sklearn import linear_model

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)
```
