# Загрузка набора данных

Сначала нам нужно загрузить набор данных digits из scikit-learn и разделить его на признаки и метки.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
