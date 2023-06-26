# Train and Evaluate the Self-Training Model

In this step, we will use Self-Training on 20% of the labeled data. We will randomly select 20% of the labeled data, train the model on that data, and then use the model to predict labels for the remaining unlabeled data.

```python
import numpy as np

# Select 20% of the training data
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Set the non-masked subset to be unlabeled
y_train[~y_mask] = -1

# Train and evaluate the Self-Training pipeline
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
