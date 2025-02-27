# Импортируем необходимые библиотеки

Начнём с импорта необходимых библиотек, включая `make_gaussian_quantiles` и `accuracy_score` из `sklearn.datasets`, `AdaBoostClassifier`, `DecisionTreeClassifier` из `sklearn.ensemble` и `matplotlib.pyplot`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
```
