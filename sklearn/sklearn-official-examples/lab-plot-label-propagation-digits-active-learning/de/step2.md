# Mische und teile die Daten auf

Als nächstes werden wir den Datensatz mischen und in gelabelte und ungelabelte Teile aufteilen. Wir beginnen zunächst mit nur 10 gelabelten Punkten.

```python
import numpy as np

rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

n_total_samples = len(y)
n_labeled_points = 10
unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
```
