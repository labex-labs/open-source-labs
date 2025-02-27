# Importieren der erforderlichen Bibliotheken

Wir beginnen mit dem Importieren der erforderlichen Bibliotheken, einschließlich `make_gaussian_quantiles` und `accuracy_score` aus `sklearn.datasets`, `AdaBoostClassifier`, `DecisionTreeClassifier` aus `sklearn.ensemble` und `matplotlib.pyplot`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
```
