# Charger l'ensemble de données

Tout d'abord, nous devons charger l'ensemble de données des chiffres à partir de scikit-learn et le diviser en caractéristiques et étiquettes.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
