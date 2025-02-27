# Bibliotheken importieren

Zunächst müssen wir die erforderlichen Bibliotheken für dieses Lab importieren, einschließlich scikit-learn.

```python
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```