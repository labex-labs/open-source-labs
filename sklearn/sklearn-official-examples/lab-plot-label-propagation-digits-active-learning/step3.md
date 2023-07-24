# Train Label Propagation Model

We will now train a label propagation model with the labeled data points and use it to predict the labels of the remaining unlabeled data points.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
