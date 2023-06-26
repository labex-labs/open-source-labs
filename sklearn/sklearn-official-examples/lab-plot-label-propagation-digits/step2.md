# Prepare Data for Semi-Supervised Learning

We select 340 samples and only 40 of these samples are associated with a known label. We store the indices of the 300 other samples for which we are not supposed to know their labels. We then shuffle the labels so that the unlabeled samples are marked with -1.

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```
