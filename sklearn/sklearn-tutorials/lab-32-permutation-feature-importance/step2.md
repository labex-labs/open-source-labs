# Train the model

Next, we will train a regression model on the training data. In this example, we will use a Ridge regression model.

```python
from sklearn.linear_model import Ridge

# Train the Ridge regression model
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```
