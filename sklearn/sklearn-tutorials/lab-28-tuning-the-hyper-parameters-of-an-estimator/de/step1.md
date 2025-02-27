# Importieren der erforderlichen Bibliotheken

Zunächst müssen wir die erforderlichen Bibliotheken für unsere Analyse importieren. Wir werden `sklearn.model_selection` verwenden, um die Hyperparameteroptimierung durchzuführen.

```python
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
```
