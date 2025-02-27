# Lade den Datensatz

Zunächst müssen wir den Digits-Datensatz aus scikit-learn laden und ihn in Features und Labels unterteilen.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
