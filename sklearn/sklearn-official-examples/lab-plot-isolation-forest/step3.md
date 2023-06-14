# Train the Model

We will train an Isolation Forest model with the training data.

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```


