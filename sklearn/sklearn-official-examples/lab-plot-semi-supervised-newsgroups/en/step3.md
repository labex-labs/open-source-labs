# Train and Evaluate the Supervised Model

In this step, we will split the dataset into training and testing sets, and then train and evaluate the supervised model pipeline we created in Step 2.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Split the dataset into training and testing sets
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train and evaluate the supervised model pipeline
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
