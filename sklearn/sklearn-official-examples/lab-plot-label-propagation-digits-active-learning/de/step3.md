# Trainiere das Labelpropagation-Modell

Wir werden nun ein Labelpropagation-Modell mit den gelabelten Datenpunkten trainieren und es verwenden, um die Labels der verbleibenden ungelabelten Datenpunkte vorherzusagen.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
