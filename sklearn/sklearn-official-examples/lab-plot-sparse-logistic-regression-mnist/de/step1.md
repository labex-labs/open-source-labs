# Bibliotheken importieren

Wir beginnen, indem wir die erforderlichen Bibliotheken für dieses Lab importieren. Wir werden die scikit-learn-Bibliothek verwenden, um den Datensatz abzurufen, das Modell zu trainieren und die Leistung des Modells zu bewerten.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```
