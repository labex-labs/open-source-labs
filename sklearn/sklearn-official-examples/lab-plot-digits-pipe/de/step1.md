# Importieren der erforderlichen Bibliotheken

Wir importieren zunächst die erforderlichen Bibliotheken für die Implementierung des Workflows.

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
```
