# Настройка классификаторов Label Spreading

Мы настроим три классификатора Label Spreading с разными процентами помеченных данных: 30%, 50% и 100%. Label Spreading - это алгоритм полуподдерживаемого обучения, который распространяет метки из помеченных в не помеченные точки данных на основе сходства между ними.

```python
from sklearn.semi_supervised import LabelSpreading

# Set up the Label Spreading classifiers
rng = np.random.RandomState(0)
y_rand = rng.rand(y.shape[0])
y_30 = np.copy(y)
y_30[y_rand < 0.3] = -1  # set random samples to be unlabeled
y_50 = np.copy(y)
y_50[y_rand < 0.5] = -1
ls30 = (LabelSpreading().fit(X, y_30), y_30, "Label Spreading 30% data")
ls50 = (LabelSpreading().fit(X, y_50), y_50, "Label Spreading 50% data")
ls100 = (LabelSpreading().fit(X, y), y, "Label Spreading 100% data")
```
