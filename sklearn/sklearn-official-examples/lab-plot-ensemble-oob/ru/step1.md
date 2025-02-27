# Импортируем необходимые библиотеки

Начнем с импорта необходимых библиотек, включая scikit-learn, NumPy и Matplotlib. Также установим значение случайного состояния, чтобы обеспечить воспроизводимость результатов.

```python
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 123
```
